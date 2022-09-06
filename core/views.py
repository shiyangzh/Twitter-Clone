from django.shortcuts import render, redirect
from core.models import Tweet, HashTag
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.


def splash(request):
    if request.user.is_authenticated:
        return redirect('/home')

    return render(request, "splash.html")


def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    if request.method == "POST":
        print(request.POST["body"])
        body = request.POST["body"]
        tweet = Tweet.objects.create(body=body, author=request.user)
        split = body.split(" ")
        for word in split:
            if word[:1] == '#':
                if not HashTag.objects.all().filter(name=word[1:]).exists():
                    hashtag = HashTag.objects.create(name=word[1:])
                    hashtag.post.add(tweet)
                    hashtag.count += 1
                    hashtag.save()
                else:
                    hashtag = HashTag.objects.get(name=word[1:])
                    hashtag.post.add(tweet)
                    hashtag.count += 1
                    hashtag.save()

    tweets = Tweet.objects.all().order_by("-created_at")
    hashtag = HashTag.objects.all().order_by("-count")
    return render(request, "home.html", {"tweets": tweets, "hashtag": hashtag})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect('/login?error=failure')

    return render(request, 'accounts.html', {})


def logout_(request):
    logout(request)
    return redirect("/login")


def signup_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST['email']
        user = User.objects.create_user(username=request.POST['username'],
                                        email=request.POST['email'],
                                        password=request.POST['password'])
        login(request, user)
        return redirect('/')
    return render(request, 'accounts.html')


def delete_(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    tweet.delete()

    split = tweet.body.split(" ")
    for word in split:
        if word[:1] == '#':
            hashtag = HashTag.objects.get(name=word[1:])
            if hashtag.count > 1:
                hashtag.post.remove(tweet)
                hashtag.count -= 1
                hashtag.save()
            else:
                hashtag.delete()

    return redirect('/')


def like_view(request):
    tweet = Tweet.objects.get(id=request.GET['id'])
    if tweet.likes.filter(id=request.user.id).exists():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)
    return redirect("/")


def profile_view(request):
    tweets = Tweet.objects.filter(author=request.GET['id']).order_by("-created_at")
    name = User.objects.get(id=request.GET['id'])
    return render(request, 'profile.html', {"tweets": tweets, "name": name})


def tag_view(request):
    # tweets = HashTag.objects.filter(post=request.GET['name'])
    hashtag = HashTag.objects.get(name=request.GET['id'])
    tags = {}
    # for tag in hashtag:
    # counter = 0
    # for tweet in hashtag.post.all():
    #     tags[counter] = tweet
    #     print(counter)
    #     counter += 1
    # tags = []
    # for tag in hashtag:
    #     tags.append(tag.post)
    return render(request, 'hashtag.html', {"hashtag": hashtag, "tags": tags})
