from django.test import Client
from django.contrib.auth.models import User

####################
#   login view     #
####################


class TestLogin:

    client = Client()

    def test_login(self):

        response = self.client.get("/login/")

        assert response.status_code == 200
        assert response.templates[0].name == "registration/login.html"
        assert response.templates[1].name == "joueur/base.html"

