from django.db import models


class Rank(models.Model):
    class Meta:
        verbose_name = "звание"
        verbose_name_plural = "звания"

    name = models.CharField(max_length=50, verbose_name="Название")

    def __str__(self):
        return self.name


class Position(models.Model):
    class Meta:
        verbose_name = "должность"
        verbose_name_plural = "должности"

    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name


class LESSON_TIME:
    TIME = [
        ("8:00", "9:35"),
        ("9:50", "11:25"),
        ("11:40", "13:15"),
        ("13:30", "15:05"),
        ("15:20", "16:55"),
        ("17:10", "18:45"),
        ("19:00", "20:35"),
        ("20:50", "22:25"),
    ]

    DAY = (
        ("mon", "Понедельник"),
        ("tue", "Вторник"),
        ("wed", "Среда"),
        ("thu", "Четверг"),
        ("fri", "Пятница"),
        ("sat", "Суббота"),
    )

    @classmethod
    def TIME_verbose(cls):
        return {x: "{} - {}".format(cls.TIME[x][0], cls.TIME[x][1]) for x in range(0, 8)}


# Create your models here.
class Professor(models.Model):
    class Meta:
        verbose_name = "преподаватель"
        verbose_name_plural = "преподаватели"

    name = models.CharField(max_length=100, verbose_name="ФИО")
    position = models.ForeignKey('Position', verbose_name="Должность")
    rank = models.ForeignKey('Rank', verbose_name="Звание")

    def __str__(self):
        return "{} {}".format(self.rank, self.name)


class Faculty(models.Model):
    class Meta:
        verbose_name = "факультет"
        verbose_name_plural = "факультеты"

    name = models.CharField(max_length=100, verbose_name="Имя")
    key = models.CharField(max_length=10, verbose_name="Кодовое название")

    def __str__(self):
        return self.name


class LectureRoom(models.Model):
    class Meta:
        verbose_name = "аудитория"
        verbose_name_plural = "аудитории"

    name = models.CharField(max_length=10, verbose_name="Название")

    def __str__(self):
        return self.name


class StudyGroup(models.Model):
    class Meta:
        verbose_name = "группа"
        verbose_name_plural = "группы"

    name = models.CharField(max_length=100, verbose_name="Имя")
    faculty = models.ForeignKey('Faculty', verbose_name="Факультет")

    def __str__(self):
        return self.name


class StudySubject(models.Model):
    class Meta:
        verbose_name = "предмет"
        verbose_name_plural = "предметы"

    name = models.CharField("Имя", max_length=100)
    type = models.CharField("Вид", max_length=20, choices=(("lect", "Лекция"), ("pract", "Практика")))

    def __str__(self):
        return "{}({})".format(self.name, self.type)

class Lesson(models.Model):
    lesson_number = models.IntegerField(choices=LESSON_TIME.TIME_verbose().items(), verbose_name="Пара")
    subject = models.ForeignKey('StudySubject', verbose_name="Предмет")
    day = models.ForeignKey("DaySchedule")
    professor = models.ForeignKey("Professor", verbose_name="Преподаватель")
    room = models.ForeignKey("LectureRoom", verbose_name="Аудитория")

    def verbose_lesson_time(self):
        return LESSON_TIME.TIME[self.lesson_number]

class DaySchedule(models.Model):
    class Meta:
        verbose_name = "расписание на день"
        verbose_name_plural = "расписание на день"

    week = models.CharField(max_length=5, verbose_name="Неделя", choices=(("1", "1"), ("2", "2")))
    day = models.CharField(max_length=20, verbose_name="День", choices=LESSON_TIME.DAY)
    group = models.ForeignKey("StudyGroup", verbose_name="Группа")
