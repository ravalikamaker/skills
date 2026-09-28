# Current accepted delivery contract

This synthetic contract applies to the current CLI and Python API.

- The CLI's default attempt limit is three (accepted change from one).
- A positive limit allows at most that many calls; stop after the first success.
- A zero or negative limit raises ValueError before calling the sender.
- The Python API returns True on success and False after exhaustion.

The README is user guidance and must reflect this current contract.
