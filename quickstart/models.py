from __future__ import unicode_literals

from django.db import models


class Hostel(models.Model):
    hostel_name = models.CharField(max_length=100, blank=False, null=True)
    rooms = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return self.hostel_name


class Notices(models.Model):
    notices = models.FileField(blank=True, null=True)


class Gallery(models.Model):
    photos = models.ImageField(blank=True, null=True)


class Room(models.Model):
    FLOOR_CHOICES = (
        ('0', "Ground Floor"),
        ('1', "1st Floor"),
        ('2', "2nd Floor"),
        ('3', "3rd Floor"),
        ('4', "4th Floor"),
    )
    ROOM_SIZE = (
        ('1', "Single Seater"),
        ('2', "Double Seater"),
        ('3', "Triple Seater"),
    )
    ROOM_TYPE = (
        ("NON-AC", "NON-AC"),
        ("AC", "AC"),
    )

    room_no = models.IntegerField(blank=True, null=True)
    floor = models.CharField(max_length=15, choices=FLOOR_CHOICES, default='1')
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    is_vacant = models.BooleanField(default=False)
    room_size = models.CharField(max_length=15, choices=ROOM_SIZE, default='1')
    room_type = models.CharField(max_length=15, choices=ROOM_TYPE, default="NON_AC")

    def __str__(self):
        return self.hostel.hostel_name + " " + str(self.room_no)