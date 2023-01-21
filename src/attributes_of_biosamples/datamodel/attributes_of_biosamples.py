# Auto generated from attributes_of_biosamples.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-01-20T23:44:59
# Schema: attributes-of-biosamples
#
# id: https://w3id.org/microbiomedata/attributes-of-biosamples
# description: Attributes of Environmental Biosamples
# license: MIT

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
MIXS = CurieNamespace('MIXS', 'http://w3id.org/mixs/')
AOB = CurieNamespace('aob', 'http://example.com/')
ATTRIBUTES_OF_BIOSAMPLES = CurieNamespace('attributes_of_biosamples', 'https://w3id.org/microbiomedata/attributes-of-biosamples/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SUGGESTION_ONLY = CurieNamespace('suggestion_only', 'http://example.com/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ATTRIBUTES_OF_BIOSAMPLES


# Types
class DecimalDegree(float):
    """ A decimal degree expresses latitude or longitude as decimal fractions """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "DecimalDegree"
    type_model_uri = ATTRIBUTES_OF_BIOSAMPLES.DecimalDegree


# Class references
class BiosampleId(extended_str):
    pass


class MeetingId(extended_str):
    pass


@dataclass
class Biosample(YAMLRoot):
    """
    something you can collect from the environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AOB.Biosample
    class_class_curie: ClassVar[str] = "aob:Biosample"
    class_name: ClassVar[str] = "Biosample"
    class_model_uri: ClassVar[URIRef] = ATTRIBUTES_OF_BIOSAMPLES.Biosample

    id: Union[str, BiosampleId] = None
    intval: int = None
    sometimes_absent: str = "present"
    depth: Optional[str] = None
    lat: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)

        if self._is_empty(self.intval):
            self.MissingRequiredField("intval")
        if not isinstance(self.intval, int):
            self.intval = int(self.intval)

        if self._is_empty(self.sometimes_absent):
            self.MissingRequiredField("sometimes_absent")
        if not isinstance(self.sometimes_absent, str):
            self.sometimes_absent = str(self.sometimes_absent)

        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        if self.lat is not None and not isinstance(self.lat, float):
            self.lat = float(self.lat)

        super().__post_init__(**kwargs)


@dataclass
class Collection(YAMLRoot):
    """
    a collection of collections
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AOB.Collection
    class_class_curie: ClassVar[str] = "aob:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = ATTRIBUTES_OF_BIOSAMPLES.Collection

    biosamples: Optional[Union[Dict[Union[str, BiosampleId], Union[dict, Biosample]], List[Union[dict, Biosample]]]] = empty_dict()
    meetings: Optional[Union[Dict[Union[str, MeetingId], Union[dict, "Meeting"]], List[Union[dict, "Meeting"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="biosamples", slot_type=Biosample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="meetings", slot_type=Meeting, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Meeting(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AOB.Meeting
    class_class_curie: ClassVar[str] = "aob:Meeting"
    class_name: ClassVar[str] = "Meeting"
    class_model_uri: ClassVar[URIRef] = ATTRIBUTES_OF_BIOSAMPLES.Meeting

    id: Union[str, MeetingId] = None
    meeting_info: Optional[Union[str, "COMPASSPOINTS"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MeetingId):
            self.id = MeetingId(self.id)

        if self.meeting_info is not None and not isinstance(self.meeting_info, COMPASSPOINTS):
            self.meeting_info = COMPASSPOINTS(self.meeting_info)

        super().__post_init__(**kwargs)


# Enumerations
class COMPASSPOINTS(EnumDefinitionImpl):

    east = PermissibleValue(text="east")
    north = PermissibleValue(text="north")
    south = PermissibleValue(text="south")
    west = PermissibleValue(text="west")

    _defn = EnumDefinition(
        name="COMPASSPOINTS",
    )

class TIMESOFDAY(EnumDefinitionImpl):

    afternoon = PermissibleValue(text="afternoon")
    evening = PermissibleValue(text="evening")
    morning = PermissibleValue(text="morning")
    night = PermissibleValue(text="night")

    _defn = EnumDefinition(
        name="TIMESOFDAY",
    )

# Slots
class slots:
    pass

slots.depth = Slot(uri=AOB.depth, name="depth", curie=AOB.curie('depth'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.depth, domain=None, range=Optional[str])

slots.biosamples = Slot(uri=AOB.biosamples, name="biosamples", curie=AOB.curie('biosamples'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.biosamples, domain=None, range=Optional[Union[Dict[Union[str, BiosampleId], Union[dict, Biosample]], List[Union[dict, Biosample]]]])

slots.id = Slot(uri=AOB.id, name="id", curie=AOB.curie('id'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.id, domain=None, range=URIRef)

slots.depth_in_meters = Slot(uri=AOB.depth_in_meters, name="depth_in_meters", curie=AOB.curie('depth_in_meters'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.depth_in_meters, domain=None, range=Optional[float])

slots.intval = Slot(uri=AOB.intval, name="intval", curie=AOB.curie('intval'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.intval, domain=None, range=int)

slots.intlist = Slot(uri=AOB.intlist, name="intlist", curie=AOB.curie('intlist'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.intlist, domain=None, range=Optional[Union[int, List[int]]])

slots.sometimes_absent = Slot(uri=AOB.sometimes_absent, name="sometimes_absent", curie=AOB.curie('sometimes_absent'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.sometimes_absent, domain=None, range=str)

slots.lat = Slot(uri=AOB.lat, name="lat", curie=AOB.curie('lat'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.lat, domain=None, range=Optional[float])

slots.experimental_slot = Slot(uri=AOB.experimental_slot, name="experimental_slot", curie=AOB.curie('experimental_slot'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.experimental_slot, domain=None, range=Optional[str])

slots.meeting_info = Slot(uri=AOB.meeting_info, name="meeting_info", curie=AOB.curie('meeting_info'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.meeting_info, domain=None, range=Optional[Union[str, "COMPASSPOINTS"]])

slots.meetings = Slot(uri=AOB.meetings, name="meetings", curie=AOB.curie('meetings'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.meetings, domain=None, range=Optional[Union[Dict[Union[str, MeetingId], Union[dict, Meeting]], List[Union[dict, Meeting]]]])