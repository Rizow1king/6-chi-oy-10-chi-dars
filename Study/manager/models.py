from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nomi')
    photo = models.ImageField(upload_to="course", verbose_name='Rasmi', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Qoshilgan vaqti')
    views = models.IntegerField(verbose_name="ko'rilgan soni", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural = 'Kurslar'
        ordering = ['-id']


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Darsni nomi')
    teacher = models.CharField(max_length=100, verbose_name="O'qituvchi ismi")
    theme = models.TextField(default="Darsni mavzusi: qo'shilmagan", blank=True, null=True,
                             verbose_name='Darsni mavzusi')
    homework = models.TextField(default='Darsni qatatdan korish va ozingiz uchun konspekt qiling',
                                verbose_name='Uyga vazifa')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    published = models.BooleanField(default=True, verbose_name='Bolganligi')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Qaysi kursga boglangani')
    student_count = models.IntegerField(verbose_name="O'quvchilar soni", default=10)
    photo = models.ImageField(upload_to='lessons.photos', verbose_name='Rasmi', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dars'
        verbose_name_plural = 'Darslar'
        ordering = ["-id"]
