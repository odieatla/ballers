# Imports
import json
from django.contrib.auth import authenticate, login
from tastypie import http
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation
from court.forms import LoginForm
 
 
class LoginResource(ModelResource):
    """ Resource that will signin a user."""
 
    class Meta:
        resource_name = "login"
        allowed_methods = ['get', 'post']
        validation = FormValidation(form_class=LoginForm)
        always_return_data = True
 
    def obj_create(self, bundle, **kwargs):
 
        if not self.is_valid(bundle):
            errors = json.dumps(bundle.errors)
            raise http.ImmediateHttpResponse(response=http.HttpBadRequest(errors))

        user = authenticate(username=bundle.data["username"],
                           password=bundle.data["password"])
        login(bundle.request, user)

        return bundle
