from .views import homepage, about
from django.urls import path 
from .views import prizing
from .views import contact
from . views import profile
from . views import fav_anime
from . views import disliked_anime
from . views import read_Artical
from.views import create_artical 
from.views import create_character
from.views import create_techqnique
from.views import show_all_characters
from .views import show_all_techniques
from.views import show_1_character
from.views import show_1_technique
from.views import edit_character
from.views import edit_teqnique
from .views import delete_character
from.views import delete_technique
urlpatterns = [
    path("Athif/", homepage, name="homepage"),
    path("Gojo/", about, name="about"),
    path ("luffy/", prizing, name="prizing"),
    path ("Naruto/", contact, name="contact"),
    path ("Geto/", profile, name="profile"),
    path ("Saitama/", fav_anime, name="fav_anime"),
    path ("Sukuna/",disliked_anime , name="disliked_anime"),
    path ("shadow/<int:number>" ,read_Artical, name="read"),
    path ("Zoro/",create_artical, name="create"),
    path ("Sao/",create_character, name="character"),
    path ("Toji/",create_techqnique, name="Technique"),
     path ("Diablo/",show_all_characters, name="show_allchar"),
     path ("Isagi/",show_all_techniques,name= "show_alltech"),
     path ("Goku/<int:id>",show_1_character,name= "show_1char"),
     path ("Maki/<int:id>",show_1_technique,name= "show_1tech"),
     path ("Baka/<int:id>",edit_character,name= "edit_char"),
     path ("Jinwoo/<int:id>",edit_teqnique,name= "edit_tech"),
     path ("Delete/<int:id>",delete_character,name="delete_character"),
     path ("kirito/<int:id>",delete_technique,name="delete_technique")

     

]
