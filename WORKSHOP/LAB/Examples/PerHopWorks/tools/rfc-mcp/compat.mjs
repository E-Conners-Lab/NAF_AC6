/**
 * Documented local compatibility repair for @mjpitz/mcp-rfc 0.2504.4.
 * Upstream still owns MCP tools, network retrieval, cache and response handling.
 * Repair only the legacy RFC HTML section extraction for RFC Editor's current page.
 * No facts, RFC answers or document text are hardcoded here.
 */
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { JSDOM } = require('jsdom');
const upstreamUrl = new URL('./node_modules/@mjpitz/mcp-rfc/build/', import.meta.url);
const { default: service } = await import(new URL('services/rfcService.js', upstreamUrl));
const original = service.parseHtmlRfc.bind(service);
service.parseHtmlRfc = function (html, number, url) {
  const result = original(html, number, url);
  if (result.sections.length) return result;
  const doc = new JSDOM(html).window.document;
  const root = doc.querySelector('#rfc-content');
  if (!root) throw new Error('RFC document container absent; refusing an empty section response');
  const markers = [...root.querySelectorAll('[id^="section-"]')]
    .filter(node => /^section-\d+(?:\.\d+)*$/.test(node.id));
  if (!markers.length) throw new Error('RFC section anchors absent; refusing an empty section response');
  result.sections = markers.map((node, i) => {
    const heading = node.closest('span.h2, span.h3, span.h4, span.h5, h2, h3, h4, h5') || node;
    const range = doc.createRange();
    range.setStartBefore(heading);
    if (i + 1 < markers.length) {
      const next = markers[i + 1];
      range.setEndBefore(next.closest('span.h2, span.h3, span.h4, span.h5, h2, h3, h4, h5') || next);
    } else range.setEnd(root, root.childNodes.length);
    return { title: heading.textContent.trim(), number: node.id.slice('section-'.length),
      content: range.toString().trim() };
  });
  const source = root.textContent;
  result.metadata.status = source.match(/^Category:\s*(Standards Track|Informational|Experimental|Best Current Practice|Historic)/m)?.[1] || result.metadata.status;
  result.metadata.compatibility_patch = 'perhop-html-anchors-v1';
  return result;
};
// Start the unchanged upstream MCP server with the repaired singleton parser.
if (!process.argv.includes('--parser-only')) await import(new URL('index.js', upstreamUrl));
export { service };
