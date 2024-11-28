from django.shortcuts import render, redirect
from django.http import HttpResponse
from menu.models import Category, MenuItem  # Import from the menu app
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Review 

def home(request):
    categories = Category.objects.all()  # Fetch all categories from the database
    return render(request, 'home.html', {'categories': categories})  # Pass categories to the template

# User registration view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after they register
            return redirect('home')  # Redirect to home or another page
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

# Submit review view
@login_required
def submit_review(request):
    if request.method == 'POST':
        review_text = request.POST.get('review')
        rating = request.POST.get('rating')

        if not review_text or not rating:
            return HttpResponse("Review text and rating are required.", status=400)

        Review.objects.create(
            review=review_text,
            rating=rating,
            user=request.user
        )

        return redirect('home')

    return render(request, 'submit_review.html')

# View all reviews
def view_reviews(request):
    reviews = Review.objects.all()  # Fetch all reviews
    return render(request, 'view_reviews.html', {'reviews': reviews})    