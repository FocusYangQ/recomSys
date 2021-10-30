from django.http import HttpResponse
from recomSys.models import testMysql


# Create your views here.

def test ( request ) :

    testmysql = testMysql.objects.all()
    print ( testmysql )

    return HttpResponse ( "test" )

