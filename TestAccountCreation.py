
from authentication.models import Account

userInfo = [
	{'email':'Tyler.Anderson@credibly.me', 'username':'Tyler.Anderson','password':'qwerty'},
	{'email':'Logan.Katseanas@credibly.me', 'username':'Logan.Katseanas','password':'qwerty'},
	{'email':'Shawna.Bowmen@credibly.me', 'username':'Shawna.Bowmen','password':'qwerty'},
	{'email':'Rony.Delisca@credibly.me', 'username':'Rony.Delisca','password':'qwerty'},
	{'email':'Zach.Logan@credibly.me', 'username':'Zach.Logan','password':'qwerty'},
	]
for user in userInfo:
	Account.objects.create(email=user['email'], username=user['username'], password=user['password'])

posts



