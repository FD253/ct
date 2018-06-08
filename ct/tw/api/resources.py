from tastypie.authorization import Authorization, DjangoAuthorization, ReadOnlyAuthorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS, Resource
from tw.models import Tweet, TwitterUser, Credential
from tastypie.authentication import Authentication, ApiKeyAuthentication
import twitter


class CreateCredentialsResource(ModelResource):
    class Meta:
        queryset = Credential.objects.all()
        allowed_methods = ['post']
        resource_name = 'credentials'
        authentication = Authentication()
        authorization = Authorization()


class UserResource(ModelResource):
    class Meta:
        queryset = TwitterUser.objects.all()
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        resource_name = 'user'
        filtering = {
            'user': ALL,
        }
        excludes = ['email', 'password', 'is_superuser', 'is_staff', 'date_joined', 
                'first_name', 'id', 'is_active', 'last_login', 'last_name']


class TweetResource(ModelResource):
    published = fields.BooleanField(default=False)
    pub_datetime = fields.DateTimeField(null=True, blank=True)
    user = fields.ForeignKey(UserResource, 'user')
    image1 = fields.FileField(attribute="image1")
    image2 = fields.FileField(attribute="image2")
    image3 = fields.FileField(attribute="image3")
    image4 = fields.FileField(attribute="image4")

    class Meta:
        queryset = Tweet.objects.select_related('user').all()
        resource_name = 'tweet'
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'pub_datetime': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        allowed_methods = ['post']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle, request=None):
        bundle.obj.user = TwitterUser.objects.get(pk=bundle.request.user.id)
        return bundle 
