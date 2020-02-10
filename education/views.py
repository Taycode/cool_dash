from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import BookSerializer, CourseSerializer
from .models import Book, Course


class BookView(APIView):

    serializer_class = BookSerializer

    @staticmethod
    def post(request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request, pk):

        if pk:

            try:
                book = Book.objects.get(pk=pk)
            except Book.DoesNotExist:
                book = None

            if book is not None:
                serializer = BookSerializer(book)
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                data = {"error": "Not found"}
                return Response(data, status=status.HTTP_404_NOT_FOUND)

        else:

            data = {"error": "No pk specified"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class SearchCourseView(APIView):

    @staticmethod
    def get(request):
        department = request.GET.get('department')
        part = request.GET.get('part')
        course = Course.objects.all()
        if department:
            course = course.filter(Q(department__name__iexact=department))
        if part:
            course = course.filter(Q(part__iexact=str(part)))

        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchBookView(APIView):

    @staticmethod
    def get(request):
        course = request.GET.get('course')
        books = Book.objects.all()
        if course:
            books = books.filter(Q(courses=course))

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CourseView(APIView):

    @staticmethod
    def get(request, code):
        if code:
            course = Course.objects.get(course_code__iexact=code)
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=status.HTTP_200_OK)
