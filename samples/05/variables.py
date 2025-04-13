print("hello world")
print("")
print("this is a string")

#this is a comment
print("")

#String Variables
skill="devOps"
print(skill) #devOps
print("")

#Integer Variables
NUM=10 #all caps is a constant
print(NUM) #10
print("")

#Lists []
tools=["git","docker","kubernetes", "K8s", "Terraform", 90]

print(tools) #['git', 'docker', 'kubernetes', 'K8s', 'Terraform', 90]
print(tools[0]) #git
print(tools[-1]) #90
print(tools[0:3]) #['git', 'docker', 'kubernetes']
print("")

#Tuplets ()
tools=("git","docker","kubernetes", "K8s", "Terraform", 90)

print(tools) #('git', 'docker', 'kubernetes', 'K8s', 'Terraform', 90)
print(tools[0]) #git
print(tools[-1]) #90
print(tools[0:3]) #('git', 'docker', 'kubernetes')
print(tools[3:5]) #('K8s', 'Terraform')
print(tools[0:3][1]) #docker
print("")

#dictionaries {}
devops={
    "skill":"devOps",
    "year":2025,
    "gitOps": "", 
}

print(devops) #{'skill': 'devOps', 'year': 2025, 'gitOps': ''}
print(devops["skill"]) #devOps
print(devops["year"]) #2025
print(devops["gitOps"]) #empty string
print("")

