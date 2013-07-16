# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.template.loaders.app_directories import app_template_dirs
import os
from django.utils.translation import ugettext_lazy as _


TEMPLATE_DIR = getattr(settings,"SMARTPAGES_TEMPLATE_DIR", "smartpages")


class Tags(models.Model):
    tag = models.CharField(max_length="64")
    description = models.TextField(blank=True)


class Block(models.Model):
    content = models.TextField(_("Content"), default="")
    text_content = models.TextField(_("Text only content"))
    key = models.TextField(_("Block identifier"), default=None)
    desc = models.CharField(_("User description"), max_length="512")


class BlockVersions(models.Model):
    content = models.TextField(_("Content"))
    timestamp = models.DateTimeField(_("Creation timestamp"), auto_now_add=True)
    block = models.ForeignKey(Block)


class Page(models.Model):
    slug = models.CharField(_("Slug"), max_length=128)
    template = models.CharField(_("Template"), max_length=512, blank=True)
    content = models.TextField(_("Content"), default="")
    title = models.CharField(_("Page title"), max_length=256)
    h1 = models.CharField(_("Page H1"), max_length=256, blank=True)
    description = models.CharField(_("Page H1"), max_length=256, blank=True)
    is_published = models.BooleanField(_("Published page on site "), default=True)
    in_menu = models.BooleanField(_("Show in menu")default=True)


class PageVersion(models.Model):

    page = models.ForeignKey(Page)
    timestamp = models.DateTimeField(u"Метка бэкапа",auto_now_add=True)

    slug = models.CharField(max_length=128)
    template = models.CharField(max_length=512, blank=True)
    content = models.TextField()
    title = models.CharField(max_length=256)
    h1 = models.CharField(max_length=256, blank=True)
    description = models.CharField(max_length=256, blank=True)


class Templates(models.Model):
    template = models.CharField(max_length=256)
    name = models.CharField(max_length=32,default="")
    filters = models.TextField(default="")

    def __unicode__(self):
        if self.name:
            return "%s <%s>" % (self.name, self.template)
        else:
            return "<%s>" % (self.template,)

    @classmethod
    def update(cls):

        for template_dir in (settings.TEMPLATE_DIRS + app_template_dirs):

            print template_dir
            for dir, dirnames, filenames in os.walk(template_dir):
                probable_dir = os.path.join(dir, TEMPLATE_DIR)
                if os.path.isdir(probable_dir):
                    print probable_dir
                    for dir, dirnames, filenames in os.walk(probable_dir):
                        print dir, dirnames, filenames




class Redirects(models.Model):
    url_from = models.CharField(max_length=1024)
    url_to = models.CharField(max_length=1024, blank=True)
    page_to = models.ForeignKey(Page, blank=True)
    description = models.TextField(blank=True)
