from django.core.exceptions import ValidationError
from django.db import models
from django.core import validators
import re
from django.contrib.auth.hashers import make_password, check_password
from datetime import date, datetime, timedelta



MIN_FIELD_LENGHT = 2
def ValidarLongitudMinima(cadena):
    if len(cadena) < MIN_FIELD_LENGHT:
        raise ValidationError(
            f'Error: {cadena} deberia tener mas de {MIN_FIELD_LENGHT} caracteres'
        )

def ValidarLongitudPassword(cadena):
    if len(cadena) < 8:
        raise ValidationError(
            f'Error: la contraseña debe ser mayor a 8 caracteres'
        )




def validarEmail(cadena):
    #valida que el email tenga el formato correcto
    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if not EMAIL_REGEX.match(cadena):          
        raise ValidationError(
            f'Error de formato: {cadena} no es un e-mail valido'
        )
    #valida que el email no se repita
    
    for s in User.objects.all():
            # se usa .lower() para ovbiar las mayúsculas en la comparación de palabras
            if cadena.lower() == s.email.lower(): 
                raise ValidationError(
                f'Error: el email {cadena} ya existe en nuestros registros!'
                )

# .label_tag(attrs={'class': 'text-danger'})
def validarFecha(fecha):
    print(fecha)
    date_today = date.today() #fecha hoy 
    birth_date = str(fecha).split('-')
    # valida la edad mayor a 13 años
    birth_year = int(birth_date[0]) #año nacimieno
    birth_month = int(birth_date[1]) #mes de nacimiento
    birth_day = int(birth_date[2]) #día de nacimiento

    
    print(birth_date)
    birth_date_user = date(birth_year, birth_month, birth_day )
    days_has_passed = (date_today-birth_date_user).days
    if days_has_passed < (365.2425*13):
            raise ValidationError(
            f'Error: la fecha de nacimiento debe ser mayor de 13 años'
            )




# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45, blank=False, null=False, validators=[ValidarLongitudMinima])
    last_name = models.CharField(max_length=45, blank=False, null=False, validators=[ValidarLongitudMinima] )
    birth_date = models.DateField(validators=[validarFecha])
    email = models.CharField(max_length=50, validators=[validarEmail])
    password = models.CharField(max_length=100, validators=[ValidarLongitudPassword])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # liked_books = a una lista de libros que le gustan a un usuario determinado
    # books_uploaded = una lista de libros cargados por un usuario determinado

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    @staticmethod
    def authenticate(email, password):
        user = User.objects.filter(email = email)
        print ('user', user)
        #buscar si hay un email en la base de datos
        if len(user) == 1:
            #si existe un email asociado
            #se extra el usuario (se supone que debe ser uno solo por sus validaciones)
            user = user[0]
            bd_password = user.password
            if check_password(password, bd_password): #convierte los hash y los comparas
                return user
        print("usuario incorrecto")
        
        return None 

    





