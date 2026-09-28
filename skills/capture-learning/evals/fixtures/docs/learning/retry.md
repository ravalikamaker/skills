# Retry observation
- Kind: observed fact
- Applies when: synthetic queue fixture, revision 1
- Finding and cause: A repeated submission produced two items; cause unknown.
- Evidence: evidence/retry-v1.txt
- Reuse: Check request identity before assuming retries are safe.
