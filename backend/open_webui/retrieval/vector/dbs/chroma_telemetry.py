import posthog
from chromadb.telemetry.product.posthog import Posthog


class OpenWebUIPosthog(Posthog):
    def __init__(self, system):
        super().__init__(system)
        if not posthog.project_api_key and not posthog.api_key:
            posthog.project_api_key = "phc_YeUxaojbKk5KPi8hNlx1bBKHzuZ4FDtl67kH1blv8Bh"
        if not posthog.api_key:
            posthog.api_key = posthog.project_api_key
