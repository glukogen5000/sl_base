from django.contrib.auth.models import User
from django.db import models
from model_utils import Choices

import datetime
import os


# def generate_unique_name(path):
#     def apper(instance, filename):
#         extension = "." + filename.split('.')[-1]
#         basename = filename.split('.')[0]
#         suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
#         new_filename = "_".join([basename, suffix]) + extension
#         return os.path.join(path, new_filename)
#     return apper
#
# def upload_location(instance, filename):
#     name, ext = os.path.splitext(filename)
#     path = f'media/{instance.slug}'
#     suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
#     new_filename = "_".join([name, suffix]) + ext
#     path = path + new_filename
#     return path


class Contractor(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250, null=True, blank=True)
    telephone = models.CharField(verbose_name='Телефон', max_length=250, null=True, blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=250, null=True, blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ItemProject(models.Model):
    yes_no = Choices('Да', 'Нет')
    mrf = models.CharField(verbose_name='МРФ', max_length=250, null=True, blank=True)
    rf = models.CharField(verbose_name='РФ', max_length=250, null=True, blank=True)
    subjectRF = models.CharField(verbose_name='Субьект РФ', max_length=250, null=True, blank=True)
    address = models.CharField(verbose_name='Адрес', max_length=250, null=True, blank=True)
    num_access_link = models.CharField(verbose_name='Количество узлов доступа и связи', max_length=250, null=True,
                                       blank=True)
    status_item = Choices('не начат', 'проблемы с допуском', 'в работе', 'СМР заевершен', 'принят', 'КС подписаны')
    status = models.CharField(choices=status_item, verbose_name='Статус', max_length=250, null=True, blank=True)
    contractor = models.ForeignKey(Contractor, null=True, blank=True, on_delete=models.SET_NULL)
    access = models.CharField(choices=yes_no, verbose_name='Допуск', max_length=250, null=True, blank=True)
    date_access_SMR = models.DateField(verbose_name='Фактическая дата получения согласований/допуска на СМР',
                                       null=True, blank=True)
    obemy_podany = models.CharField(choices=yes_no, verbose_name='Объемы поданы', max_length=250, null=True, blank=True)
    ready_smr = models.CharField(choices=yes_no, verbose_name='СМР выполнены', max_length=250, null=True, blank=True)
    data_priemki_rtk = models.DateField(verbose_name='Дата приемки РТК',
                                        null=True, blank=True)
    foto_montaj_upload = models.CharField(choices=yes_no, verbose_name='ФОТО монтажа + схемы для ИД приложены',
                                          max_length=250, null=True, blank=True)
    smr_ready = models.CharField(choices=yes_no, verbose_name='СМР выполнены', max_length=250, null=True, blank=True)
    rtk_ready = models.CharField(choices=yes_no, verbose_name='Примека РТК проведена', max_length=250, null=True,
                                 blank=True)
    id_ready = models.CharField(choices=yes_no, verbose_name='ИД загружена', max_length=250, null=True,
                                blank=True)
    act_ready = models.CharField(choices=yes_no, verbose_name='ИД загружена', max_length=250, null=True,
                                 blank=True)
    plan_data_ready_smr = models.DateField(verbose_name='Плановая дата завершение СМР',
                                           null=True, blank=True)
    data_ready_from_dogovor = models.DateField(verbose_name='Срок завершения работ по договору',
                                               null=True, blank=True)

    komentariy = models.TextField(verbose_name='Коментарий', null=True, blank=True)

    def __str__(self):
        return self.address

# class FeedFilePhoto(models.Model):
#     file = models.FileField(upload_to=upload_location("pic"))
#     feed = models.ForeignKey(ItemProject, on_delete=models.CASCADE)


# class FeedFileAkt(models.Model):
#     file = models.FileField(upload_to=upload_location())
#     feed = models.ForeignKey(ItemProject, on_delete=models.CASCADE)
#
#
# class FeedFileID(models.Model):
#     file = models.FileField(upload_to=upload_location())
#     feed = models.ForeignKey(ItemProject, on_delete=models.CASCADE)
#
# class StatusKD(models.Model):
#     id = models.AutoField(primary_key=True)
#     StatusName = models.CharField(verbose_name='Статус', max_length=250)
#     StepNum = models.IntegerField()
#     Role1Set = models.IntegerField()
#     Role2Set = models.IntegerField()
#     Role3Set = models.IntegerField()
#     Role4Set = models.IntegerField()
#
#     def __str__(self):
#         return self.StatusName
#
#     # class Meta:
#     #     verbose_name = 'Статус '
#     #     verbose_name_plural = 'Статусы'
#
#
# class StatusID(models.Model):
#     id = models.AutoField(primary_key=True)
#     StatusName = models.CharField(verbose_name='Статус', max_length=250)
#     StepNum = models.IntegerField()
#     Role1Set = models.IntegerField()
#     Role2Set = models.IntegerField()
#     Role3Set = models.IntegerField()
#     Role4Set = models.IntegerField()
#
#     def __str__(self):
#         return self.StatusName
#
#     # class Meta:
#     #     verbose_name = 'Статус'
#     #     verbose_name_plural = 'Статусы'
#
#
# class StatusAddres(models.Model):
#     id = models.AutoField(primary_key=True)
#     StatusName = models.CharField(verbose_name='Статус', max_length=250)
#     StepNum = models.IntegerField()
#     Role1Set = models.IntegerField()
#     Role2Set = models.IntegerField()
#     Role3Set = models.IntegerField()
#     Role4Set = models.IntegerField()
#
#     def __str__(self):
#         return self.StatusName
#
#     # class Meta:
#     #     verbose_name = 'Статус'
#     #     verbose_name_plural = 'Статусы'
#
#
# class School(models.Model):
#     id = models.AutoField(primary_key=True)
#     Address = models.CharField(verbose_name='Адрес', blank=True, max_length=245)
#     District = models.CharField(verbose_name='Район', blank=True, max_length=250)
#     # FactCountOfUP
#     # FactCountOfRP
#     # Responsible - отве6тственный
#     Status_name = models.ForeignKey(StatusAddres, on_delete=models.SET_NULL, null=True)
#     StatusID = models.ForeignKey(StatusID, on_delete=models.SET_NULL, null=True)
#     StatusKD = models.ForeignKey(StatusKD, on_delete=models.SET_NULL, null=True)
#     Okrug_list = Choices('САО', 'СВАО', 'СЗАО', 'ВАО', 'ЮАО', 'ЮЗАО', 'ЮВАО', 'ЗАО')
#     AO = models.CharField(choices=Okrug_list, verbose_name='Округ', max_length=250)
#     OUnumber = models.CharField(verbose_name='OUNUm', blank=True, max_length=250)
#     Contact = models.CharField(verbose_name='Контакты', blank=True, max_length=250)
#     # OrderedCountOfUP
#     # OrderedCountOfRP
#     MontStartDate = models.DateField()
#     status_tr_list = Choices('1', '2', '3', '4', '5')
#     StatusTR = models.CharField(choices=status_tr_list, blank=True, default='-', max_length=250)
#     Name = models.CharField(verbose_name='Название', blank=True, max_length=250)
#     City = models.CharField(verbose_name='Город', blank=True, max_length=250)
#     PostIndex = models.CharField(verbose_name='Индекс', blank=True, max_length=250)
#     Note = models.CharField(verbose_name='Заметка', blank=True, max_length=250)
#     Operator_list = Choices('МГТС', '-')
#     Operator = models.CharField(choices=Operator_list, blank=True, default='-', max_length=250)
#     InstPlace = models.CharField(verbose_name='Адрес установки оборудования', blank=True, max_length=250)
#     SchoolID = models.IntegerField(default=int(0), blank=True)
#     StatusKO = models.CharField(verbose_name='', blank=True, max_length=250)
#     IP = models.GenericIPAddressField(blank=True, null=True)
#     Mask = models.IntegerField(default=int(0), blank=True)
#     VPN = models.CharField(verbose_name='МГТС VPN', blank=True, max_length=250)
#     UploadDate = models.DateField(blank=True)
#     StatusAOS = models.CharField(verbose_name='', blank=True, max_length=250)
#     MGTSPointID = models.IntegerField(default=int(0), blank=True)
#     MGTSAddress = models.CharField(verbose_name='МГТС Адрес', blank=True, max_length=250)
#     MGTSPointName = models.CharField(verbose_name='МГТС название', blank=True, max_length=250)
#     MGTSOkrug = models.CharField(verbose_name='МГТС округ', blank=True, max_length=250)
#     MGTSIP = models.GenericIPAddressField(blank=True, null=True)
#     MGTSMask = models.IntegerField(default=int(0), blank=True)
#     MGTSVPN = models.CharField(verbose_name='МГТС VPN', blank=True, max_length=250)
#     IDprinted = models.IntegerField(default=int(0), blank=True)
#     #  2911HWActCount
#     #  2960HWActCount
#     #  LNKSHWActCount
#     #  MGTSAccArcPath
#     # MGTSAccComment
#     Coords = models.CharField(verbose_name='Координаты', blank=True, max_length=250)
#     # IDprinted
#     # Uploader
