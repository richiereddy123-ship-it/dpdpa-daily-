---
title: "Navigating AI Training Data: DPDPA's Deemed Consent vs. Global Frameworks"
date: 2026-06-19 13:05:01 +0530
categories: [analysis, comparative]
tags: [DPDPA, GDPR, AI, Data Privacy, Consent, comparative]
---

The rapid proliferation of Artificial Intelligence (AI) models has brought the critical issue of training data to the forefront of privacy law. For Indian businesses and Data Fiduciaries navigating the newly enforced Digital Personal Data Protection Act, 2023 (DPDPA), understanding how to lawfully acquire and process data for AI training is paramount. This challenge is particularly acute when comparing DPDPA's consent-centric approach with the more flexible, albeit highly conditional, legitimate interests basis found in the EU's General Data Protection Regulation (GDPR) and elaborated upon by the UK Information Commissioner's Office (ICO).

## The DPDPA's Stance on AI Training Data

The DPDPA anchors personal data processing firmly on consent. Under Section 6, a Data Fiduciary must obtain clear, affirmative, and unambiguous consent from the Data Principal for processing their personal data. This consent must be specific to the purpose of processing. For AI training, especially for novel applications or broad datasets, securing such explicit consent from potentially millions of individuals can be an immense, if not impossible, undertaking.

While the DPDPA introduces "deemed consent" in Section 7, its applicability to AI training data is significantly constrained. Deemed consent applies only in specific scenarios, such as when processing is necessary for the performance of a contract, for public interest, or for purposes for which the Data Principal has "voluntarily provided" their personal data and "it is reasonably expected" that they would provide consent. The challenge for AI training is that the "reasonable expectation" clause might not extend to repurposing existing data for unforeseen AI models, particularly if the original purpose was different. Furthermore, the DPDPA's purpose limitation principle (Section 5) dictates that personal data can only be processed for the purpose for which consent was given or deemed. Repurposing data collected for a specific service to train a new, unrelated AI model without fresh consent or a clearly applicable deemed consent ground would likely constitute a violation. This makes the DPDPA potentially stricter in its requirements for explicit consent for AI training data compared to its global counterparts, creating a potential "gap" for broad-scale AI development.

## GDPR's Legitimate Interests for AI Development

In contrast to the DPDPA's narrower deemed consent, the GDPR provides a broader legal basis for processing personal data: "legitimate interests" under Article 6(1)(f). This provision allows data processing without explicit consent if it is "necessary for the purposes of the legitimate interests pursued by the controller or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject which require protection of personal data."

For AI training, legitimate interests often serve as the preferred legal basis, particularly when obtaining explicit consent is impractical or disproportionate, and the processing does not involve sensitive data or high-risk profiling. However, relying on Article 6(1)(f) is not a carte blanche. It necessitates a rigorous three-part balancing test:
1.  **Identify a legitimate interest:** For AI, this could be innovation, product improvement, or research.
2.  **Necessity:** The processing must be necessary to achieve that interest.
3.  **Balancing test:** The controller's legitimate interests must not be overridden by the fundamental rights and freedoms of the data subjects. This requires a careful assessment of the impact on individuals, the nature of the data, and the safeguards in place.

Compared to the DPDPA, GDPR offers more flexibility for AI training by providing a non-consent-based ground that can accommodate broader data uses, provided the balancing test is diligently applied. This makes the GDPR "looser" in its initial gateway for processing but demands robust accountability and impact assessment.

## UK ICO Guidance: Practical Application and Safeguards

The UK, post-Brexit, largely retains the GDPR's principles, with the UK GDPR and the Data Protection Act 2018. The UK Information Commissioner's Office (ICO) has provided extensive guidance on AI and data protection, offering practical insights into applying these principles. The ICO strongly advocates for a thorough Legitimate Interests Assessment (LIA) when using Article 6(1)(f) for AI training.

The ICO's guidance emphasizes several key considerations that effectively make the application of legitimate interests "stricter" in practice:
*   **Transparency:** Data Fiduciaries must be transparent about how data is used for AI training, even when relying on legitimate interests (Article 13/14). This includes explaining the types of data, the purposes of AI training, and the safeguards in place.
*   **Data Minimisation:** Only necessary data should be used, and anonymisation or pseudonymisation should be employed where possible.
*   **Purpose Limitation:** Data collected for one purpose should not be automatically repurposed for AI training without careful consideration and justification under the LIA.
*   **Risk Mitigation:** Implementing robust security measures, conducting Data Protection Impact Assessments (DPIAs), and offering clear data subject rights (e.g., the right to object under Article 21) are crucial.

The ICO's stance highlights that while legitimate interests offer a pathway, the accompanying obligations for transparency, accountability, and risk mitigation are substantial. This practical guidance underscores that while the legal basis might be more flexible than DPDPA's deemed consent, the operational burden of compliance remains high.

## Comparative Gaps and Overlaps

The primary distinction lies in the foundational legal bases. The DPDPA's emphasis on explicit consent and narrowly defined deemed consent creates a higher bar for repurposing existing datasets for AI training, potentially limiting innovation that relies on broad data aggregation without explicit, specific consent. In contrast, GDPR's legitimate interests provide a more elastic framework, allowing for a broader range of AI development activities, provided a rigorous balancing test and robust safeguards are in place.

All three frameworks converge on core data protection principles: purpose limitation, data minimisation, accuracy, and security. Transparency is also a common thread, though the practicalities of explaining AI model training to data subjects remain a complex challenge across jurisdictions. The DPDPA is arguably stricter on the initial gateway for processing for AI training, whereas GDPR/UK ICO, while offering a broader gateway, impose significant ongoing compliance and accountability requirements.

**Practical takeaway**

Indian businesses, General Counsels, and Data Protection Officers engaged in AI development must meticulously review their data acquisition and processing strategies under the DPDPA. Relying solely on a broad interpretation of "deemed consent" for AI training, especially for novel applications, carries significant risk. Prioritise obtaining explicit, specific consent wherever feasible. For situations where deemed consent might be considered, ensure the processing aligns strictly with the specified grounds in Section 7 and the "reasonable expectation" clause is robustly justifiable. For operations extending to the EU or UK, understand that while legitimate interests (GDPR Article 6(1)(f)) offer flexibility, they demand a comprehensive Legitimate Interests Assessment, transparent communication, and strong mitigation strategies as per ICO guidance. Regardless of jurisdiction, embed data protection by design, conduct thorough DPIAs, and champion data minimisation and purpose limitation to build trustworthy AI. Proactive engagement with the Data Protection Board of India for specific guidance on AI training data will be crucial as the regulatory landscape evolves.
