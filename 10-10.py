"""ADC, Support, Jungle"""

import random

# Top 10 most played champions per role in platinum
adc_meta = ["Ezreal", "Jhin", "Ashe", "Caitlyn", "Kai'Sa", "Samira", "Vayne", "Lucian", "Senna", "Miss Fortune"]
support_meta = ["Thresh", "Lulu", "Leona", "Yuumi", "Morgana", "Pantheon", "Nautilus", "Senna", "Blitzcrank", "Pyke"]
jungle_meta = ["Nidalee", "Nunu", "Graves", "Kha'Zix", "Hecarim", "Kayn", "Ekko", "Evelynn", "Lillia", "Lee Sin"]

n = random.randint(0, 9)
adc_pick = adc_meta[n]
print("ADC Pick:", adc_pick)

n = random.randint(0, 9)
support_pick = support_meta[n]
print("Support Pick:", support_pick)

n = random.randint(0, 9)
jungle_pick = jungle_meta[n]
print("Jungle Pick:", jungle_pick)