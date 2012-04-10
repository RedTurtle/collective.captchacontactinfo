from zope.interface import Interface


class IContactinfoSupportView(Interface):
    """Interface for SiteSearchView"""

    def getPolicyText():
        """
        Return the policy text
        """
