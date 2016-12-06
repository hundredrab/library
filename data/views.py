from django.views import generic
from .models import Book,Subject
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class IndexView(generic.ListView):
    template_name = 'data/index.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Book.objects.all()


class DetailView(generic.DetailView):
    model = Book
    template_name = 'data/detail.html'


class BookCreate(CreateView):
    model = Book
    fields = ['author', 'title', 'subject', 'image']


class BookUpdate(UpdateView):
    model = Book
    fields = ['author', 'title', 'subject', 'image']


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('data:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'data/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('data:index')











"""from django.shortcuts import render,get_object_or_404
from .models import Book


# Create your views here.
def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books' : all_books,
    }
    return render(request,'data/index.html',context)

def detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'data/detail.html', {'book' : book})

"""


