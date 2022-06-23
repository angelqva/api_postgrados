from rest_framework.routers import DefaultRouter
from users.views import UserView, LogoutView
from estudiantes.views import EstudianteView
from profesores.views import ProfesorView
from postgrados.views import NacionalView, InternacionalView
from reportes.views import ReporteView

router = DefaultRouter()
router.register(prefix='users', basename='users', viewset=UserView)
router.register(prefix='logout-token', basename='logout', viewset=LogoutView)
router.register(prefix='estudiantes', basename='estudiantes',
                viewset=EstudianteView)
router.register(prefix='profesores', basename='profesores',
                viewset=ProfesorView)
router.register(prefix='postgrados_nacionales',
                basename='postgrados_nacionales', viewset=NacionalView)
router.register(prefix='postgrados_internacionales',
                basename='postgrados_internacionales', viewset=InternacionalView)
router.register(prefix='reportes',
                basename='reportes', viewset=ReporteView)
