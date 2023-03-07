array = [{
    'palabra': 'hola',
    'video': 'hola/dsdsadads/DSDSAdssIVIVADP/download.mp4'
},
         {
    'palabra': 'como estas',
    'video': 'como estas/dsdsadads/DSDSAdssIVIVADP/download.mp4'
},
         {
    'palabra': 'yea',
    'video': 'yea/dsdsadads/DSDSAdssIVIVADP/download.mp4'
},
         {
    'palabra': 'waa',
    'video': 'waa/dsdsadads/DSDSAdssIVIVADP/download.mp4'
},
         {
    'palabra': 'okey',
    'video': 'okey/dsdsadads/DSDSAdssIVIVADP/download.mp4'
},
         {
    'palabra': 'sobres',
    'video': 'sobres/dsdsadads/DSDSAdssIVIVADP/download.mp4'
},
         {
    'palabra': 'bueno',
    'video': 'bueno/dsdsadads/DSDSAdssIVIVADP/download.mp4'
},
         {
    'palabra': 'good',
    'video': 'good/dsdsadads/DSDSAdssIVIVADP/download.mp4'
}]


res = input("Dame una palabra: ")
for i in array:
  if res == i['palabra']:
    print(i['video'])
  
 


