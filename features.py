classes = ['glioma', 'meningioma', 'pituitary', 'no_tumor']

formation = {
    'glioma': 'Formed by uncontrolled growth of glial cells, often due to genetic mutations like IDH.',
    'meningioma': 'Arises from the meninges (brain covering layers), usually benign and slow-growing.',
    'pituitary': 'Develops in the pituitary gland, often affecting hormone production.',
    'no_tumor': 'No abnormal growth detected – normal brain tissue.'
}

treatments = {
    'glioma': 'Surgery followed by Temozolomide chemotherapy and radiation (typically 6-12 months).',
    'meningioma': 'Observation or surgical removal; radiation if inoperable.',
    'pituitary': 'Transsphenoidal surgery or medication to control hormones.',
    'no_tumor': 'No treatment required.'
}

survival_est = {
    'glioma': '12-36 months depending on grade (high-grade shorter).',
    'meningioma': 'Excellent – often >10 years.',
    'pituitary': 'Very good prognosis after treatment.',
    'no_tumor': 'Normal lifespan.'
}