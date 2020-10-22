# -*- coding: utf-8 -*-
"""see: https://www.hl7.org/fhir/extensibility.html
Extensibility feature for FHIR Primitive Data Types.
"""
__author__ = "Md Nazrul Islam<email2nazrul>"

import typing

from pydantic import Field, root_validator
from pydantic.errors import MissingError
from pydantic.error_wrappers import ErrorWrapper, ValidationError

from . import fhirabstractmodel, fhirtypes


class FHIRPrimitiveExtension(fhirabstractmodel.FHIRAbstractModel):
    """"""

    resource_type = Field("FHIRPrimitiveExtension", const=True)

    id: fhirtypes.String = Field(
        None,
        alias="id",
        title="Type `String`",
        description="Unique id for inter-element referencing",
    )

    extension: typing.List[fhirtypes.ExtensionType] = Field(
        None,
        alias="extension",
        title="List of `Extension` items (represented as `dict` in JSON)",
        description="Additional content defined by implementations",
    )

    @root_validator(pre=True)
    def validate_one_of_many(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """Conditional Required Validation"""
        errors = list()
        extension = values.get("extension", None)
        fhir_comments = values.get("fhir_comments", None)

        if extension is None and fhir_comments is None:
            errors.append(ErrorWrapper(MissingError(), loc="extension"))
            raise ValidationError(errors, cls)

        return values
