from typing import Optional
from fastapi import FastAPI

from job_wrapper.api import create_api_app
from job_wrapper.health import HealthState
from job_wrapper.loader import instantiate_class_entrypoint
from job_wrapper.validate import validate_entrypoint


def create_entrypoint_app(
    model_path: str,
    class_name: Optional[str] = None,
    health_state: HealthState = None,
) -> FastAPI:
    """
    Load entrypoint from a Python module and embed it in a FastAPI app
    """
    entrypoint = instantiate_class_entrypoint(model_path, class_name)
    validate_entrypoint(entrypoint)
    if health_state is None:
        health_state = HealthState(live=True, ready=True)
    return create_api_app(entrypoint, health_state)
