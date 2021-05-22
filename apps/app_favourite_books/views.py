from django.shortcuts import redirect, render
from .models import Book
from .forms.new_book import BookForm
from .forms.update_book import UpdateBookForm
from apps.app_login_register.models import User

# Create your views here.
def dashboard(request):
    
    # si viene de un GET
    if request.method == 'GET':
        # si la sesión no existe
        if 'id' not in  request.session :
            return redirect('/')
        # si la sesión existe
        else:
            #cargar el form de ingresar el libro           
            user_selected = User.objects.get(id = int(request.session['id']) )
            #guarda los libros que le gustan al usuario
            # id_liked_books_of_user = user_selected.liked_books
            # print(id_liked_books_of_user)
            all_books = Book.objects.all()  
            context = {

                "user_selected" : user_selected,
                "all_books" : all_books,
                "BookForm" : BookForm(),
                # "user_likes" : user_likes,
                }
            return render(request, 'dashboard.html', context)
   



def addbook(request):
    # Preguntar si existe la sesión para ejecutar la acción
    if 'id' not in  request.session :
            return redirect('/')
    # si la sesión existe
    else:
        print(request.POST['title'])
        print(request.POST['description'])
        this_user = User.objects.get(id = int(request.session['id']) )
        new_book = Book.objects.create(title = request.POST['title'], description = request.POST['description'], uploaded_by = this_user)
        new_book.users_who_like.add(this_user)
        return redirect('/')

def detail(request, num):
    # Preguntar si existe la sesión
    if 'id' not in  request.session :
            return redirect('/')
    # si la sesión existe
    else:
        #obtiene el objeto a modificar
        selected_book = Book.objects.get(id = int(num))
        #obtiene el formulario con la instancia del libro a actualizar
        form = UpdateBookForm(instance=selected_book)
        #obtiene el usuario quien tienen iniciada la sesióm
        user = User.objects.get(id = int(request.session['id']))
        #obtiene la lista de usuarios a quienes les gusta este libro
        users_who_like_this_book = selected_book.users_who_like.all()
        if request.method == 'GET':
            # si el que ve el detalle es el creador
            if int(selected_book.uploaded_by.id) == int(request.session['id']):
                #guarda el formulario en el context para que pueda ser utilizado en el HTML
                context = {
                    'UpdateBookForm' : form,
                    'selected_book' : selected_book,
                    'first_name' : user.first_name,
                    'last_name' : user.last_name,
                    'email' : user.email,
                    'birth_date' : user.birth_date,
                    'id' : user.id,
                    'users_who_like_this_book' : users_who_like_this_book
                }
                return render(request, 'book_detail.html', context)
            #si es otro usuario
            else:
                context = {
                    'Book' : selected_book,
                    'first_name' : user.first_name,
                    'last_name' : user.last_name,
                    'email' : user.email,
                    'birth_date' : user.birth_date,
                    'id' : user.id,
                    'users_who_like_this_book' : users_who_like_this_book
                }
                return render(request, 'book_detail_lecture_only.html', context)
        # si es POST actualiza los datos del form 
        else:
            #guarda en una variable current_book el objeto(libro) a actualizar
            #se actualizan los campos con los datos ingresados en el formulario 
            selected_book.title = request.POST['title']
            selected_book.description = request.POST['description']
            #guarda esos cambios
            selected_book.save()
            return redirect('/books/' + num)

def delete(request, num):
    # Preguntar si existe la sesión para ejecutar la acción
    if 'id' not in  request.session :
            return redirect('/')
    # si la sesión existe
    else:
        #selecciona el libro a borrar
        book_to_delete = Book.objects.get(id= int(num))
        #borra el libro seleccionado
        book_to_delete.delete()
        return redirect('/')

def add_favourite(request, num):
    # Preguntar si existe la sesión para ejecutar la acción
    if 'id' not in  request.session :
            return redirect('/')
    # si la sesión existe
    else:
        #selecciona al usuario
        this_user = User.objects.get(id=int(request.session['id']))
        #seleccionar el libro a gustar
        likeable_book = Book.objects.get(id= int(num))
        #asignar el libro al usuario
        likeable_book.users_who_like.add(this_user)
        return redirect('/books/' + num)


def add_favourite_in_dash(request, num):
    # Preguntar si existe la sesión para ejecutar la acción
    if 'id' not in  request.session :
            return redirect('/')
    # si la sesión existe
    else:
        #selecciona al usuario
        this_user = User.objects.get(id=int(request.session['id']))
        #seleccionar el libro a gustar
        likeable_book = Book.objects.get(id= int(num))
        #asignar el libro al usuario
        likeable_book.users_who_like.add(this_user)
        return redirect('/')


def delete_favourite(request, num):
    # Preguntar si existe la sesión para ejecutar la acción
    if 'id' not in  request.session :
            return redirect('/')
    # si la sesión existe
    else:
        #selecciona al usuario
        this_user = User.objects.get(id=int(request.session['id']))
        #seleccionar el libro a gustar
        likeable_book = Book.objects.get(id= int(num))
        #asignar el libro al usuario
        likeable_book.users_who_like.remove(this_user)
        return redirect('/books/' + num)
        

def delete_favourite_in_dash(request, num):
    # Preguntar si existe la sesión para ejecutar la acción
    if 'id' not in  request.session :
            return redirect('/')
    # si la sesión existe
    else:
        #selecciona al usuario
        this_user = User.objects.get(id=int(request.session['id']))
        #seleccionar el libro a gustar
        likeable_book = Book.objects.get(id= int(num))
        #asignar el libro al usuario
        likeable_book.users_who_like.remove(this_user)
        return redirect('/')

           

