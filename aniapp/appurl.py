from .views import homepage, about
from django.urls import path 
from .views import prizing
from .views import contact
from . views import profile
from . views import fav_anime
from . views import disliked_anime
from . views import read_Artical
urlpatterns = [
    path("Athif/", homepage, name="homepage"),
    path("Gojo/", about, name="about"),
    path ("luffy/", prizing, name="prizing"),
    path ("Naruto/", contact, name="contact"),
    path ("Geto/", profile, name="profile"),
    path ("Saitama/", fav_anime, name="fav_anime"),
    path ("Sukuna/",disliked_anime , name="disliked_anime"),
    path ("shadow/" ,read_Artical, name="read")
]
