# Final RFC fact audit — 2026-11-04

Thirteen live RFC MCP `get_rfc(format="full")` calls were appended as V-0014–V-0026.
The original verification artifacts remain intact. New returned documents and status metadata are
under `research/rfc/final/`; checksums and call arguments are in `VERIFICATION.md`.

The implementation agent re-read the cited sections, including exact six-bit assignments in
Figure 3, scheduler/AQM guidance in Figure 4, the nine-class Example 3, literal meter algorithms,
and both updates supplied by the owner. Retrieval alone was not treated as verification.

Corrections made during this audit:

- F-0018 now distinguishes CS6 routing/control from CS7 reserved for possible future control use;
  its source includes §3.2 for the restriction on user traffic. Briefing wording was updated.
- F-0032 now preserves the RFC's alternative of dropping **or ECN marking** above the RED maximum.
  The game explicitly chooses dropping and does not simulate ECN marking. Briefings were updated.
- F-0025 now cites both §4.3 and §4.7 for aware/blind guidance covering both trTCM and srTCM.

RFC 4594 remains Informational. RFC 5865 adds capacity-admitted telephony and video guidance;
that behavior is not simulated. RFC 8622 replaces historical CS1 with LE (000001). The campaign and
showcase explicitly identify their original 2006 profile; no claim is made that CS1 remains the
current lower-effort recommendation. RFC 2598 is obsolete and RFC 3246 is used for EF.

| Fact | Rechecked source | Live verification |
|---|---|---|
| F-0001 | RFC 2474 §3 | V-0014 |
| F-0002 | RFC 3168 §5 | V-0019 |
| F-0003 | RFC 2474 §4.2.2.1 | V-0014 |
| F-0004 | RFC 2597 §6 | V-0016 |
| F-0005 | RFC 3246 §2.7 | V-0020 |
| F-0006 | RFC 2474 §4.2.2.3 | V-0014 |
| F-0007 | RFC 2475 §2.3.1 | V-0015 |
| F-0008 | RFC 2475 §2.3.3.2 | V-0015 |
| F-0009 | RFC 2475 §2.3.3.1 | V-0015 |
| F-0010 | RFC 2475 §2.3.3.4 | V-0015 |
| F-0011 | RFC 3290 §6.2 | V-0022 |
| F-0012 | RFC 3290 §7.1.1 | V-0022 |
| F-0013 | RFC 3290 §7.1.2 | V-0022 |
| F-0014 | RFC 4594 §2.3 | V-0023 |
| F-0015 | RFC 4594 §1.3 | V-0023 |
| F-0016 | RFC 4594 §1.5.3 | V-0023 |
| F-0017 | RFC 4594 §3.2 | V-0023 |
| F-0018 | RFC 4594 §3.1; §3.2 | V-0023 |
| F-0019 | RFC 2697 §3 | V-0017 |
| F-0020 | RFC 2697 §3 | V-0017 |
| F-0021 | RFC 2697 §2 | V-0017 |
| F-0022 | RFC 2698 §3 | V-0018 |
| F-0023 | RFC 2698 §3 | V-0018 |
| F-0024 | RFC 2698 §2 | V-0018 |
| F-0025 | RFC 4594 §4.3; §4.7 | V-0023 |
| F-0026 | RFC 4594 §4.7 | V-0023 |
| F-0027 | RFC 4594 §4.3 | V-0023 |
| F-0028 | RFC 4594 §2.3 | V-0023 |
| F-0029 | RFC 4594 §2.3 | V-0023 |
| F-0030 | RFC 4594 §4.3 | V-0023 |
| F-0031 | RFC 4594 §4.3 | V-0023 |
| F-0032 | RFC 4594 §4.3 | V-0023 |
| F-0033 | RFC 4594 §2.4.3 | V-0023 |
| F-0034 | RFC 5865 §3 | V-0025 |
| F-0035 | RFC 8622 §10 | V-0026 |
| F-0036 | RFC 3260 §4 | V-0021 |
| F-0037 | RFC 2474 §4.1 | V-0014 |
| F-0038 | RFC 4594 §3.2; §2.3 Figure 3 | V-0023 |
| F-0039 | RFC 4594 §4.1; §2.3 Figure 3 | V-0023 |
| F-0040 | RFC 4594 §4.2; §2.3 Figure 3 | V-0023 |
| F-0041 | RFC 4594 §4.3; §2.3 Figure 3 | V-0023 |
| F-0042 | RFC 4594 §4.4; §2.3 Figure 3 | V-0023 |
| F-0043 | RFC 4594 §4.5; §2.3 Figure 3 | V-0023 |
| F-0044 | RFC 4594 §4.6; §2.3 Figure 3 | V-0023 |
| F-0045 | RFC 4594 §4.7; §2.3 Figure 3 | V-0023 |
| F-0046 | RFC 4594 §3.3; §2.3 Figure 3 | V-0023 |
| F-0047 | RFC 4594 §4.8; §2.3 Figure 3 | V-0023 |
| F-0048 | RFC 4594 §4.9; §2.3 Figure 3 | V-0023 |

Every briefing, hint, diagnostic, introduction and Demo fact ID resolves to this ledger.
Assistant review proceeds under the owner’s continuing authorization in `content-review.md`.
