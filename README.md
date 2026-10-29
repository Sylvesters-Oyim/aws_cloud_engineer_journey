# aws_cloud_engineer_journey
My self-taught journey into AWS cloud engineering, from beginner to **AWS Certified Cloud Practitioner (CLF-C02)** and **Solutions Architect – Associate (SAA-C03)**.

## Start here
**Read the course as a website:** https://sylvesters-oyim.github.io/aws_cloud_engineer_journey/ (enabled via GitHub Pages, see below).
Offline: clone the repo and double-click `aws-course/index.html`. GitHub's file viewer only shows source code, not the rendered page.
Modules are practical, one per day: concept → analogy → diagram → lab → quiz.

### Enable the website (one-time)
Repo → Settings → Pages → Source: *Deploy from a branch* → Branch: `main` (after merging) → Folder: `/ (root)` → Save. The root `index.html` redirects to the course.

## Progress tracker
| Day | Module | Status |
|---|---|---|
| 1 | What is the cloud, really? | ⬜ |
| 2 | Create and lock down your AWS account | ⬜ |
| 3 | IAM: who can do what | ⬜ |
| 4 | Global infrastructure and the AWS CLI | ⬜ |
| 5 | EC2: your first server | ⬜ |
| 6 | S3 (weekend lab) | ⬜ |
| 7 | EBS, pricing models, Week 1 review | ⬜ |
| 8 | VPC: your private network | ⬜ |
| 9 | Private subnets, NAT, SG vs NACL | ⬜ |
| 10 | DNS and Route 53 | ⬜ |
| 11 | CloudFront + private S3 | ⬜ |
| 12 | Security services: KMS, CloudTrail, WAF | ⬜ |
| 13 | Weekend project: secure two-tier network + CloudWatch | ⬜ |
| 14 | Week 2 review + 25-question mini-exam | ⬜ |
| 15+ | Week 3: databases, serverless, load balancing, Auto Scaling | 🔜 next |

Mark ✅ as you finish each day, and put your own console screenshots in [`aws-course/evidence/`](aws-course/evidence).

## Milestones
- [ ] Week 1 complete
- [ ] Week 2 complete
- [ ] Book CLF-C02 exam (end of week 4)
- [ ] Pass CLF-C02
- [ ] Pass SAA-C03

## Repo map
- `Phase_01: FOUNDATIONS/`: Linux foundations
- `nginx-lab/`: local nginx lab (reused on Day 5 and 6)
- `aws-course/`: the course (HTML modules, `_src` sources, `build.py` to regenerate)

## Rules for this repo
No access keys, `.pem` files, or account IDs in commits.

## Acknowledgment
The course material (lessons, diagrams, quizzes) was drafted with the help of Claude, an AI assistant by Anthropic. I run and verify every lab myself and keep my own notes and evidence in this repo.
