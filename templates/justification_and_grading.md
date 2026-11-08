# Justification structure and Merit / Distinction scaffolds

> **Important:** I do not have the official wording of your seven grade-determining items. Copy the exact
> criterion text from your brief / your Notion guide into the `CRITERION:` line of each scaffold below.
> Your notes say Merit needs a Pass on every criterion AND the "Merit" level on all seven grade-determining items.
> Always follow the brief's wording over these templates.

## The 5-part justification (use for every design/test decision)

1. **Decision** - what you chose, in one sentence.
2. **Why (threat/requirement)** - which threat or requirement it addresses. Name it (e.g. "ARP spoofing", "brief requirement 3").
3. **Evidence** - screenshot, command output, or test result that proves it works. Label it (Figure 2).
4. **Alternatives considered** - one alternative and why you did not pick it (cost, complexity, risk).
5. **Residual risk / limits** - what this does NOT protect against, and what you would add next.

Template:

> I chose **[decision]** because **[threat/requirement]**. Evidence: **[Figure N: what it shows]**.
> I considered **[alternative]** but rejected it because **[reason]**. The remaining risk is **[residual risk]**,
> which could be reduced by **[next step]**.

## Merit scaffold (repeat per grade item)

```
CRITERION: <paste exact text>
Pass level (what the criterion minimally needs): <one line>
Merit level (adds: justification + evidence + comparison): 
  - What I did: ...
  - Why this option over <alternative>: ...
  - Evidence (Figure/Table #): ...
  - Link to a standard or framework (e.g. NCSC, OWASP, MITRE ATT&CK, CIS): ...
```

## Distinction scaffold (only if time allows; adds critical evaluation)

```
CRITERION: <paste exact text>
Distinction level (adds: critical evaluation, own tooling, quantified impact):
  - Limitations of my approach and how I tested them: ...
  - Trade-offs (security vs usability vs cost) with one concrete example: ...
  - Own analysis/tooling (script name + repo link + what it found): ...
  - Quantified result (numbers, percentages, counts): ...
  - Recommendation with priority and owner: ...
```

## Sentence starters that show evaluation

- "This reduces the likelihood of X, but does not address Y, so I also..."
- "The trade-off is..., which I accepted because..."
- "Testing showed..., which contradicts my expectation that..."
- "Compared with <option>, this costs more but gives..."
- "If this control failed, the impact would be..., detected by..."

## Evidence checklist (take as you go, not at the end)

- [ ] Screenshot has the command and the result visible, with a visible time/hostname where possible
- [ ] Every figure is numbered and referred to in the text
- [ ] Hashes recorded for any sample/file used
- [ ] Commands copied into an appendix so a marker can reproduce them
- [ ] Write-up states which parts are your own work and which are adapted (cite tools/repos anyway; it costs one line)
