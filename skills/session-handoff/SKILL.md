---
name: session-handoff
description: Saves a task checkpoint before a session change, context loss, or transfer to another worker. Preserves active decisions, changes, checks, and pending actions so work can resume; excludes ordinary completion summaries and reusable lessons.
license: MIT
---

# Session Handoff

Leave the next session enough verified state to continue the active task without repeating completed work or expanding its authorized actions.

## Choose the destination

Follow an explicit user destination, then existing project or user handoff conventions within the authorized scope. Read the current task's existing checkpoint before updating it. If none exists and a local write is authorized, use a small discoverable file such as `docs/handoffs/<task-slug>.md`. An explicit request to save a handoff authorizes that scoped artifact, subject to host and memory restrictions; ordinary read-only work does not authorize file writes. When writing is not authorized, return the handoff in the response.

Inspect the destination's intended audience and repository visibility. Omit secrets, unnecessary personal details, and confidential content inappropriate for that audience. Gitignored does not mean private. If sensitive state cannot safely fit the available destination, preserve a sanitized checkpoint and state what must be retrieved through an authorized private channel. Do not overwrite unrelated notes or modify global memory, skills, or agent instructions.

## Record the state needed to resume

Recheck facts that may have changed and are quick to verify before saving. In a Git workspace, record the exact repository/worktree path, branch or detached state, HEAD commit, and staged, unstaged, and untracked paths. Distinguish owned changes from known concurrent work; mark uncertain ownership rather than guessing. Summarize important diffs without copying secret-bearing content. Do not commit, stash, reset, or clean files to make the checkpoint simpler. Outside Git, name the actual artifacts and their current state.

Record the purpose and intended beneficiary alongside the original active
outcome and latest user correction. Preserve unresolved assumptions that could
change the next decision; distinguish them from verified facts.

For consequential decisions, link relevant existing records and preserve the
context, rationale, consequences, and any superseded choice; keep proposed and
accepted choices distinct.

Include completed checks with results and artifact pointers, unresolved limits, and the next executable action. Record authorization already given and actions still outside it; never turn a proposal into approval.

If workers or processes exist, record their handles, ownership, status, output locations, and pending follow-ups. Distinguish observed running state from an assumption. Handles are hints for inspection, not guarantees that workers survive the session. Do not repeat completed work merely because a worker is no longer reachable.

Use this compact shape; omit irrelevant fields:

```markdown
# Handoff: <task> — <timestamp and timezone>
- Purpose, intended beneficiary, active outcome, and latest steering:
- Scope, non-goals, and authorized actions:
- Workspace / branch / HEAD / dirty paths and ownership:
- Decisions: context, rationale, consequences, status, and relevant records:
- Completed work, checks, results, and evidence locations:
- Live workers/processes: handle, owned task, status, output:
- Pending work, blockers, unresolved assumptions, and evidence limits:
- Next action and expected result:
- Resume checks: facts or handles that may have changed:
```

## Save and resume

Read back the saved checkpoint and verify referenced local artifacts exist, or label them unavailable. Report its path and any omitted or uncertain state. A saved file is not proof of automatic loading or successful resumption.

On resumption, compare the checkpoint with current instructions, workspace
status, relevant decision records, and available worker state before acting.
Preserve newer concurrent work and reuse still-valid evidence. Recheck the
artifact and assumptions attached to each relied-on result: changed requirements,
dependencies, configuration, or boundary conditions can invalidate a prior pass
without a source edit. Mark affected evidence stale and name the needed recheck.

Handoffs describe transient progress; reusable lessons belong in separate knowledge
notes only when their capture is authorized. An ordinary completion summary reports
finished work; this checkpoint enables resumption. Do not create a lesson note
merely because a handoff was requested.

## Worked example

Synthetic checkpoint: HEAD H1; owned change is `src/labels.ts`; unit checks passed
for H1, while integration is pending. The user authorized local label changes
only. Next action is the existing integration command.

On resume, HEAD is H2 and another contributor has modified `src/router.ts`.
Result: retain the label work, inspect the new router diff and current instructions,
and verify whether the H1 evidence still applies before continuing integration.
Do not reset the router or repeat completed checks solely because the session
changed. Record the current state and ownership uncertainty if it remains unclear.
