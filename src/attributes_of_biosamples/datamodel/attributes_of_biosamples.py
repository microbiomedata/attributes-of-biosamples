# Auto generated from attributes_of_biosamples.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-01-20T19:10:20
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
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
TEMP = CurieNamespace('TEMP', 'https://example.org/TEMP/')
ATTRIBUTES_OF_BIOSAMPLES = CurieNamespace('attributes_of_biosamples', 'https://w3id.org/microbiomedata/attributes-of-biosamples/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = ATTRIBUTES_OF_BIOSAMPLES


# Types

# Class references



@dataclass
class Biosample(YAMLRoot):
    """
    something you can collect from the environment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.Biosample
    class_class_curie: ClassVar[str] = "TEMP:Biosample"
    class_name: ClassVar[str] = "Biosample"
    class_model_uri: ClassVar[URIRef] = ATTRIBUTES_OF_BIOSAMPLES.Biosample

    depth: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.depth is not None and not isinstance(self.depth, str):
            self.depth = str(self.depth)

        super().__post_init__(**kwargs)


@dataclass
class BiosampleCollection(YAMLRoot):
    """
    a collection of Biosamples
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEMP.BiosampleCollection
    class_class_curie: ClassVar[str] = "TEMP:BiosampleCollection"
    class_name: ClassVar[str] = "BiosampleCollection"
    class_model_uri: ClassVar[URIRef] = ATTRIBUTES_OF_BIOSAMPLES.BiosampleCollection

    biosamples: Optional[Union[dict, Biosample]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.biosamples is not None and not isinstance(self.biosamples, Biosample):
            self.biosamples = Biosample(**as_dict(self.biosamples))

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.depth = Slot(uri=TEMP.depth, name="depth", curie=TEMP.curie('depth'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.depth, domain=None, range=Optional[str])

slots.biosamples = Slot(uri=TEMP.biosamples, name="biosamples", curie=TEMP.curie('biosamples'),
                   model_uri=ATTRIBUTES_OF_BIOSAMPLES.biosamples, domain=None, range=Optional[Union[dict, Biosample]])