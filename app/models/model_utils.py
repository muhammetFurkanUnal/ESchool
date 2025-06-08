from typing import Union, List
from pydantic import BaseModel

def raw_to_model(raw: Union[dict, List[dict]], model: BaseModel):
    
    """
    this function casts what returned from database query into a pydantic model.
    can differentiate if query returned a list or a single element.
    
    """
    
    if isinstance(raw, list):
        return [model(**element) for element in raw]
    elif raw == None:
        return None
    else:
        raise ValueError("Input must be a dict or a list of dicts")