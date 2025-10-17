from django.contrib.gis import admin
from .models import Point_vente
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class Point_venteAdmin(LeafletGeoAdmin):
    # pass
    list_display = ('p1', 'p102', 'p103', 'p8', 'p16', 'p17', 'p15', 'p26', 'p10')

    fieldsets = (
        ('Localisation', {  # First section
            'fields': ('p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7')
        }),
        ('Identification', {  # First section
            'fields': ('p102', 'p103', 'p8', 'p9', 'p16', 'p17', 'p18', 'p19', 'p20', 'p21', 'p22', 'p23', 'p24', 'p25', 'p57')
        }),
        ('Activité', {  # First section
            'fields': ('p26', 'p27', 'p28', 'p29', 'p50', 'p58')
        }),
        ('Lieu de vente', {  # First section
            'fields': ('p14', 'p10', 'p11', 'p30', 'p56', 'p37', 'p31', 'p32', 'p33', 'p34', 'p35', 'p36', 'p12', 'p13')
        }),
        ('Eau Courante', {  # First section
            'fields': ('p38', 'p39', 'p40')
        }),
        ('Toilettes aménagées', {  # First section
            'fields': ('p41', 'p42', 'p43')
        }),
        ('Bacs à ordure', {  # First section
            'fields': ('p44', 'p45', 'p46')
        }),
        ('Electricité', {  # First section
            'fields': ('p47', 'p48', 'p49', 'p51')
        }),
        ('Magasin', {  # First section
            'fields': ('p52', 'p53', 'p54', 'p55')
        }),
        ('Produits/Services', {  # First section
            'fields': ('p15', 'p59', 'p60', 'p61', 'p62', 'p63', 'p64', 'p65', 'p66', 'p67', 'p68', 'p69', 'p70')
        }),
        ('Préjudices', {  # First section
            'fields': ('p73', 'p74', 'p75', 'p76', 'p77', 'p78', 'p79', 'p80', 'p81', 'p82', 'p83', 'p84')
        }),
        ('Accompagnements', {  # First section
            'fields': ('p85', 'p86', 'p71', 'p72', 'p87', 'p88', 'p89', 'p90', 'p91', 'p93', 'p95', 'p96', 'p97')
        }),
        ('Attentes', {  # First section
            'fields': ('p92', 'p94', 'p98', 'p99', 'p100')
        }),
    )




admin.site.register(Point_vente, Point_venteAdmin)
