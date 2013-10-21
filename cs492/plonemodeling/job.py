from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable


from cs492.plonemodeling import MessageFactory as _


# Interface class; used to define content-type schema.

class IJob(form.Schema, IImageScaleTraversable):
    """
    Job which needs to be run on scientific model
    """

    # If you want a schema-defined interface, delete the model.load
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/job.xml to define the content type.

    # form.model("models/job.xml")
    title = schema.TextLine(
            title=_(u"Job name"),
        )

    description = schema.Text(
            title=_(u"Job summary"),
        )
    startString = schema.Text(
            title=_(u"command used to start the model")
        )
    start = schema.Datetime(
            title=_(u"Start time"),
            required=False,
        )

    end = schema.Datetime(
            title=_(u"End time"),
            required=False,
        )

    details = RichText(
            title=_(u"Details"),
            description=_(u"Details about the program"),
            required=False,
        )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Job(Container):
    grok.implements(IJob)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# job_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IJob)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
