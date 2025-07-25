from django.shortcuts import render
from django.shortcuts import HttpResponse
from app.models import Students as st
from app.models import Books
from app.models import LibId 
from app.models import Branch

# Create your views here.

def manage(req):
    return render(req, "main.html")

#Adding new branch=================================================
def branch(req):
    return render(req, "main.html", {"branch":"branch"})

def addbranch(req):
    print("Adding Branch:\n")
    if req.method == "POST":
        branch=req.POST.get('addbranch')
        print(branch)
    Branch.objects.create(branch_name=branch)
    return render(req, "main.html", {"note":"Branch Added Successfully"})

# library and it's new id generation ===============================================================

def library(req):
    return render(req, "main.html", {"library":"library"})

def addlib_id(req):
    print("Adding new library id:\n")
    
    #adding data
    if req.method=="POST":
        lib_id=req.POST.get("addlib_id")
        print(lib_id)
    LibId.objects.create(lib_id=lib_id)
    return render(req, "main.html", {"note":"New Library ID Generated!"})

#Student data and assigning branch and library id 

def student(req):

    #libID and branch data transfer to html dynamically
    lid_data=LibId.objects.all()
    branch_data=Branch.objects.all()
    return render(req, "main.html", {"student":"student", "lid_data": lid_data, "branch_data": branch_data })

def studata(req):
    print("Adding Student Info to Lib_ID\n")
    if req.method=="POST":
        x=req.POST.get
        name=x("name")
        email=x("email")
        contact=x("contact")
        branch=x("branch")
        branch_obj=Branch.objects.get(branch_name=branch)
        libid=x("lib_id")
        libid_obj=LibId.objects.get(lib_id=libid)
    print(name,"-" , email,"-" , contact,"-" , branch,"-" , branch_obj,"-" ,  libid,"-" , libid_obj)
    st.objects.create(name=name, email=email, contact=contact, branch=branch_obj, lib_id=libid_obj)
    return render(req, "main.html", {"note":"Library id Assigned"})



def book(req):
    return render(req, "main.html", {"book": "book"})

def addbook(req):
    print("Adding Book:\n")
    if req.method=="POST":
        book=req.POST.get("book")
        author=req.POST.get("author")
    print(book,"-" , author)
    Books.objects.create(book_name=book, author=author)
    return render(req, "main.html", {"note":"Book Added to Library Successfully"})


def issue(req):

    #sending LibId and books data to html dynamically
    libid_data=LibId.objects.all()
    books_data=Books.objects.all()
    return render(req, "main.html", {"issue":"issue", "libid_data":libid_data, "books_data":books_data})

def book_issued(req):
    print("Book Issued\n")
    if req.method=="POST":
        lib_id=req.POST.get("library_id")
        libid_obj=LibId.objects.get(lib_id=lib_id)
        issued_b_name=req.POST.get("issuedb_name")
        issued_b_obj=Books.objects.get(book_name=issued_b_name)
        issued_b_id=issued_b_obj.id
        print(issued_b_id)
    print(lib_id,"-" , libid_obj,"-" ,issued_b_name,"-" , issued_b_obj)
    libid_obj.issued_book.add(issued_b_id)
    return render(req, "main.html", {"note": "Book Issued Successfully"} )
    

#DATA ACCESSING=============================================================================


def data(req):

    students=st.objects.all()
    branch_data=Branch.objects.all()
    for i in branch_data:
        x=i.stu_branch.all()
        # for j in x:
        #     print(j.name)

    lib_id_data=LibId.objects.all()
    # return HttpResponse(students)
    return render(req, "data.html", {"students": students, "branch_data": branch_data,"branch_obj": x ,"lib_id_data": lib_id_data})