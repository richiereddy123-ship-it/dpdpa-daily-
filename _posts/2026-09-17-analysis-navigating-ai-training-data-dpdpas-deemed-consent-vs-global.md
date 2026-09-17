---
title: "Navigating AI Training Data: DPDPA's Deemed Consent vs. Global Frameworks"
date: 2026-09-17 13:05:55 +0530
categories: [analysis, comparative]
tags: [AI, DPDPA, GDPR, UK ICO, Data Privacy, comparative]
---

As of September 17, 2026, the landscape of AI development continues its rapid ascent, bringing with it complex questions about the provenance and legality of training data. For Indian businesses and data fiduciaries, understanding the nuances of the Digital Personal Data Protection Act, 2023 (DPDPA) in relation to global benchmarks like the EU's General Data Protection Regulation (GDPR) and UK ICO guidance is paramount. The core challenge lies in establishing a valid legal basis for processing personal data for AI training, particularly when explicit consent is impractical for vast, historical datasets.

## DPDPA's Framework: Deemed Consent and its Ambiguity for AI
The DPDPA, India's foundational data protection law, introduces the concept of "deemed consent" as a legal basis for processing personal data under specific "legitimate uses" outlined in Section 7. These include purposes for which the Data Principal has voluntarily provided their personal data, or where processing is necessary for public interest (Section 7(d)), employment purposes, or reasonable expectations (Section 7(c)). While deemed consent aims to simplify compliance in certain scenarios, its application to the large-scale, often retrospective, collection and processing of data for AI training remains a significant grey area.

The DPDPA does not explicitly address AI training data acquisition. This silence creates a gap: data fiduciaries might attempt to rely on "public interest" or "reasonable expectation" under deemed consent. However, the scope of what constitutes "public interest" in the context of AI development, or what a Data Principal might "reasonably expect" regarding their data being used for machine learning, is yet to be definitively interpreted by the Data Protection Board of India (DPBI). Without clear guidelines, relying solely on deemed consent for AI training, especially for data not directly provided for that purpose, carries inherent risks. For sensitive personal data, DPDPA Section 9 explicitly mandates explicit consent, making deemed consent inapplicable and setting a stricter standard than for general personal data. Furthermore, sector-specific regulations from bodies like the Reserve Bank of India (RBI) or rules under the Information Technology Act, 2000 (e.g., IT Rules, 2021) may impose additional restrictions, such as data localization or content moderation requirements, indirectly impacting AI training data strategies within India.

## GDPR's Legitimate Interest: A Structured Approach
In contrast to DPDPA's deemed consent, the GDPR offers "legitimate interest" as a robust and frequently utilised legal basis for processing personal data for AI training, as per Article 6(1)(f). This basis requires controllers to conduct a thorough balancing test, weighing their legitimate interest against the fundamental rights and freedoms of the data subjects. Key considerations include:
1.  **Legitimacy of the interest**: Is the interest in developing AI a genuine, lawful, and clearly articulated purpose?
2.  **Necessity**: Is the processing of personal data truly necessary for achieving that legitimate interest? Could the AI be trained with anonymised or synthetic data instead?
3.  **Balancing test**: Does the legitimate interest override the rights and freedoms of the data subject? This involves assessing the impact on individuals, the safeguards in place (e.g., pseudonymisation, security measures), and the reasonable expectations of data subjects.

While GDPR also permits explicit consent (Article 6(1)(a)), legitimate interest is often preferred for AI training due to the sheer volume and diversity of data involved. However, for special categories of personal data (e.g., health, racial origin) under Article 9, explicit consent or a specific exception is almost always required, presenting a hurdle similar to DPDPA's Section 9.

## UK ICO's Practical Guidance: Fairness and Accountability
The UK, having largely retained the GDPR framework through the Data Protection Act 2018 (DPA 2018), provides specific guidance from the Information Commissioner's Office (ICO) on AI and data protection. The ICO's approach emphasises practicality, transparency, and accountability. While aligning with GDPR's legitimate interest as a primary legal basis, the ICO stresses the importance of adhering to all data protection principles, particularly fairness, transparency, and data minimisation.

The ICO guidance highlights the need for organisations to:
*   Clearly define the purpose of AI training and ensure it is lawful and fair.
*   Conduct Data Protection Impact Assessments (DPIAs) for high-risk AI systems, documenting the legitimate interest assessment in detail.
*   Implement robust anonymisation or pseudonymisation techniques where possible.
*   Ensure transparency with data subjects about how their data is used for AI, even when relying on legitimate interest.
*   Establish clear data retention policies for training data.

The ICO's emphasis on documenting the balancing test and demonstrating accountability provides a more granular roadmap for compliance than what is currently explicit in the DPDPA for AI training.

## Comparative Landscape and Key Differences
Comparing these frameworks reveals distinct approaches and areas of divergence:

*   **Legal Basis for AI Training**: DPDPA's reliance on "deemed consent" for "legitimate uses" (Section 7) is *less defined* for AI training than GDPR's "legitimate interest" (Article 6(1)(f)), which mandates a structured balancing test. This makes DPDPA *potentially looser* in interpretation but *silent* on specific AI guidance, leading to uncertainty.
*   **Transparency and Accountability**: All frameworks require transparency. However, GDPR and UK ICO guidance offer more explicit expectations for documenting the legal basis, conducting DPIAs, and explaining AI data use to data subjects. DPDPA's specific requirements for transparency around deemed consent for AI are still evolving.
*   **Sensitive Data**: Both DPDPA (Section 9) and GDPR (Article 9) impose *stricter* requirements, typically mandating explicit consent or specific legal grounds for processing sensitive personal data, making them broadly similar in this regard.
*   **Guidance Specificity**: The UK ICO provides the most *specific and practical guidance* on AI training data, offering a risk-based approach that helps organisations navigate compliance. DPDPA is currently *silent* on such specific guidance, awaiting DPBI interpretations.

In essence, while DPDPA offers flexibility through deemed consent, this flexibility comes with a current lack of clarity for AI training. GDPR provides a more structured, albeit potentially more demanding, framework via legitimate interest. UK ICO builds on this with practical, risk-based advice.

## Practical Takeaway
For Indian businesses, General Counsels, and Data Protection Officers engaged in AI development, a proactive and cautious approach is essential. Given the DPDPA's current ambiguity regarding AI training data under deemed consent, consider these actions:
1.  **Prioritise Explicit Consent**: Wherever feasible, especially for new data collection or sensitive personal data (DPDPA Section 9), obtain explicit consent.
2.  **Document Legitimate Use**: If relying on deemed consent under DPDPA Section 7, rigorously document your assessment of how AI training aligns with "public interest" (Section 7(d)) or "reasonable expectation" (Section 7(c)), anticipating future scrutiny from the DPBI.
3.  **Adopt GDPR Best Practices**: Even if not directly subject to GDPR, consider implementing a legitimate interest assessment (LIA) similar to Article 6(1)(f) and conduct Data Protection Impact Assessments (DPIAs) for AI projects. This demonstrates a commitment to privacy by design and helps mitigate risks.
4.  **Enhance Transparency**: Clearly inform data principals about the use of their data for AI training in your privacy notices, even if relying on deemed consent.
5.  **Monitor DPBI Guidance**: Stay vigilant for any forthcoming clarifications or specific guidance from the Data Protection Board of India on AI training data, as this will shape future compliance efforts.
6.  **Data Minimisation and Security**: Implement robust data minimisation techniques, anonymisation, or pseudonymisation, and ensure strong security measures are in place for all AI training data.
