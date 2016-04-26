from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from authentication.models import Account

examplePosts = [
	{'author':'Tyler.Anderson', 'password':'qwerty', 'post': {'recipient':'Josiah.Colt','content':'I have known Josiah for almost 15 years as his very close friend. His love and inspiration bleeds onto everyone he comes in contact with. I have seen his drive and ambition carry him to accomplish his life goals and help those closest accomplish their goals. Josiah is not one to settle for normal. He has the skills and know how to reach very high levels of success.'}
	},
	{'author':'Logan.Katseanas', 'password':'qwerty', 'post': {'recipient':'Josiah.Colt','content':'I have known Josiah for almost 15 years as his very close friend. His love and inspiration bleeds onto everyone he comes in contact with. I have seen his drive and ambition carry him to accomplish his life goals and help those closest accomplish their goals. Josiah is not one to settle for normal. He has the skills and know how to reach very high levels of success.'}
	},
	{'author':'Shawna.Bowmen', 'password':'qwerty', 'post': {'recipient':'Josiah.Colt','content':'Thank you for being such a light to everyone around you. And always being there if anyone needs help. Thanks for being awesome!'}
	},
	{'author':'Rony.Delisca', 'password':'qwerty', 'post': {'recipient':'Josiah.Colt','content':'Josiah Colt is a workout warrior. He finds ways to push through the impenetrable wall, no matter how treacherous the obstacle.'}
	},
	{'author':'Zach.Logan', 'password':'qwerty', 'post': {'recipient':'Josiah.Colt','content':'I have had the pleasure of knowing Josiah for two years now and it has been one awesome ride. He is a good friend who is always there when you need him plus he is always down for a good time. I can honestly call Josiah a true friend.'}
	}
	]

#examplePost = examplePosts[0]
for examplePost in examplePosts:
	# If we want to force authentication
	user = Account.objects.get(username=examplePost['author'])
	client = APIClient()
	client.force_authenticate(user=user)

	#token = Token.objects.get(user__username=examplePost['author'])
	#client = APIClient()
	#client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

	client.login(username=examplePost['author'], password=examplePost['password'])
	print(examplePost['post'])
	# This creates redundant entries.
	client.post('/api/v1/posts/', examplePost['post'], format='json')

	client.logout()

