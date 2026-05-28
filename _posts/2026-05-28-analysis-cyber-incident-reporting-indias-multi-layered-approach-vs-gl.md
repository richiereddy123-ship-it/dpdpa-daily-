---
title: "Cyber Incident Reporting: India's Multi-Layered Approach vs. Global Frameworks"
date: 2026-05-28 12:05:42 +0530
categories: [analysis, comparative]
tags: [cybersecurity, incident reporting, DPDPA, CERT-In, NIS2, SEC]
---

The landscape of cybersecurity incident reporting has grown increasingly complex, driven by escalating threats and evolving regulatory demands. For Indian businesses navigating this environment, understanding domestic obligations, particularly the CERT-In Directions and the newly effective Data Protection Board of India (DPB) under the Digital Personal Data Protection Act (DPDPA), alongside global benchmarks like the EU's NIS2 Directive and the US SEC's cyber rules, is crucial. This analysis anchors on India's framework to compare its strictness, flexibility, and silent areas against these international counterparts.

## Scope and Applicability: Broad vs. Sectoral Focus

India's primary cybersecurity incident reporting mandate stems from the CERT-In Directions issued under Section 70B of the Information Technology Act, 2000. These apply broadly to "all service providers, data centres, body corporate and Government organisations." This wide net covers virtually any entity operating in India, with specific emphasis on critical infrastructure, virtual asset service providers, and cloud service providers. In contrast, the EU's NIS2 Directive (Directive (EU) 2022/2555) adopts a more sector-specific approach, categorising "essential entities" (e.g., energy, transport, health) and "important entities" (e.g., digital providers, food) across 18 defined sectors, typically based on size thresholds. The US SEC's cyber rules, specifically Item 1.05 of Regulation S-K and Rule 30 of Regulation S-P, primarily target publicly traded companies (registrants) and registered investment advisers/funds, respectively, focusing on incidents that could materially impact investors.

Compared to NIS2's sectoral and size-based criteria, or the SEC's public company focus, CERT-In's Directions cast a significantly wider net, encompassing a vast array of entities without explicit size or sector limitations for general incident reporting. This makes the Indian framework arguably more encompassing in its initial reach for "any body corporate."

## Reporting Triggers and Timelines: India's Strictest Window

The most striking difference lies in reporting timelines. CERT-In Directions (Para 3) mandate reporting "any cybersecurity incident" within a mere **6 hours** of noticing or being brought to notice. This is an exceptionally tight window, requiring immediate internal detection and assessment capabilities. Specific types of incidents, such as data breaches, ransomware attacks, and unauthorised access, are explicitly listed as reportable.

NIS2 (Art. 20) requires an initial notification of a "significant incident" to the competent authority within **24 hours** of becoming aware. This must be followed by an updated assessment within **72 hours**, and a final report within **one month**. A "significant incident" is defined by criteria such as causing significant operational disruption, financial loss, or affecting other entities. The SEC's Item 1.05 of Regulation S-K for public companies requires disclosure of a "material cybersecurity incident" within **4 business days** of determining materiality. For investment advisers and funds, Rule 30 of Regulation S-P mandates reporting "significant" cybersecurity incidents within **48 hours**.

India's 6-hour window is unequivocally the strictest among these frameworks, demanding an extremely rapid response and initial assessment. While NIS2 and SEC rules introduce concepts of "significant" or "materiality," which can allow for a brief internal assessment period, CERT-In's "any incident" language suggests a lower threshold for initial reporting, prioritising speed over a detailed preliminary analysis.

## Information Requirements and Follow-up Obligations

CERT-In Directions (Para 3) require the initial report to include the incident's type, nature, impact, and actions taken. Beyond this, entities must provide information as sought by CERT-In and cooperate fully. There isn't a prescribed multi-stage reporting structure, but continuous engagement and information sharing are implied. Additionally, CERT-In mandates log retention for 180 days (Para 5).

NIS2 (Art. 20) has a more structured multi-stage reporting process: the 24-hour notification includes a preliminary assessment, the 72-hour update provides a more detailed assessment of the incident's type, severity, potential impact, and indicators of compromise, and the one-month final report details the root cause, impact, and mitigation measures. It also requires notifying affected recipients if there is a public interest. The SEC's Form 8-K (S-K Item 1.05) mandates disclosure of the nature, scope, timing, and material impact of the incident, with updates required if previous disclosures become materially inaccurate. Rule 30 of Regulation S-P for investment entities requires details about the incident and remediation efforts.

Here, NIS2 offers the most detailed and multi-staged reporting requirements, pushing for progressive disclosure. CERT-In is less prescriptive on the initial content beyond basic details but demands ongoing cooperation. The SEC focuses on information relevant to investors' material interests.

## Interplay with Data Protection and Practical Takeaway

Beyond CERT-In, Indian businesses must also consider the Digital Personal Data Protection Act, 2023 (DPDPA). Section 17 of the DPDPA requires Data Fiduciaries to notify the Data Protection Board of India and affected Data Principals in the event of a "personal data breach." While the specific rules detailing timelines and content for DPDPA breach notifications are now in force, they generally align with global best practices, often providing a slightly longer window than CERT-In's 6 hours but still demanding prompt action. Furthermore, sectoral regulators like the Reserve Bank of India (RBI) impose their own specific and often stricter cyber incident reporting requirements for regulated financial entities, sometimes overlapping with CERT-In but with a financial sector-specific lens.

Globally, NIS2 coexists with the GDPR (Regulation (EU) 2016/679), where a "significant incident" under NIS2 might also constitute a "personal data breach" under GDPR (Art. 33-34), requiring notification to Data Protection Authorities within 72 hours. The SEC rules are more standalone, though data breaches might trigger other US state-level privacy laws.

**Practical takeaway:** Indian businesses, GCs, and DPOs must develop an integrated incident response plan that accounts for multiple, potentially overlapping, reporting obligations. The 6-hour CERT-In window is a critical challenge requiring highly efficient detection, assessment, and reporting mechanisms. This necessitates clear internal escalation paths, cross-functional incident response teams (IT, legal, DPO, communications), and a robust understanding of *all* applicable reporting thresholds and timelines – CERT-In for general cyber incidents, DPDPA for personal data breaches, and any relevant sectoral regulations like those from the RBI. For entities with global operations, this complexity multiplies, demanding a harmonised approach to incident management that can meet the most stringent requirements across jurisdictions.
