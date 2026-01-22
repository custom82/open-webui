from chromadb.telemetry.product import ProductTelemetryClient, ProductTelemetryEvent


class NoopProductTelemetry(ProductTelemetryClient):
    def capture(self, event: ProductTelemetryEvent) -> None:
        return None
