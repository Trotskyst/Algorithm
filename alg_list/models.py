from django.db import models
from django.template.defaultfilters import slugify as django_slugify


alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}

def slugify(s):
    """
    Overriding django slugify that allows to use russian words as well.
    """
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))

class GroupAlgorithm(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название группы алгоритма")
    slug = models.CharField(max_length=200, verbose_name="ЧПУ", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id',]

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.id)+'_'+self.name)
        super().save(*args, **kwargs)


class Algorithm(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название алгоритма")
    group = models.ForeignKey(GroupAlgorithm, related_name='group', verbose_name="Группа", on_delete=models.CASCADE)
    slug = models.CharField(max_length=200, verbose_name="ЧПУ", blank=True)

    class Meta:
        ordering = ['id',]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.id)+'_'+self.name)
        super().save(*args, **kwargs)