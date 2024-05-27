import requests   ###module to talk with API

#### Got API from Github API docs under pull  /repos/{owner}/{repo}/pulls
#### replace owner with organisation name and repo with repository name, include https://

pull = requests.get("https://api.github.com/repos/docker/compose/pulls")

#### .json converts the object into dictionary and stores in variable convert
convert = pull.json()


for user in range(len(convert)):
    print(convert[user]["user"]["login"])


  
  
  
  
  
  
  #####print(convert[5]["user"]["login"])
  ### replaced index number of dictionary using output of range stored in User via for loop
