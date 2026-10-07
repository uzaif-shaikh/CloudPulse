from datetime import datetime

from app import create_app
from app.extensions import db
from app.models import Metric


app = create_app()

with app.app_context():

    # Delete existing metric data
    Metric.query.delete()

    # Temporary metric data
    metric1 = Metric(
        server_id=1,
        cpu_usage=35.5,
        memory_usage=62.3,
        disk_usage=48.7,
        network_sent=25.4,
        network_received=18.6,
        timestamp=datetime.now()
    )

    metric2 = Metric(
        server_id=2,
        cpu_usage=52.8,
        memory_usage=71.2,
        disk_usage=55.4,
        network_sent=32.6,
        network_received=24.8,
        timestamp=datetime.now()
    )

    metric3 = Metric(
        server_id=3,
        cpu_usage=78.4,
        memory_usage=84.5,
        disk_usage=67.3,
        network_sent=45.8,
        network_received=38.2,
        timestamp=datetime.now()
    )

    metric4 = Metric(
        server_id=4,
        cpu_usage=21.7,
        memory_usage=43.6,
        disk_usage=35.8,
        network_sent=18.2,
        network_received=12.5,
        timestamp=datetime.now()
    )

    metric5 = Metric(
        server_id=5,
        cpu_usage=91.2,
        memory_usage=89.7,
        disk_usage=82.1,
        network_sent=61.4,
        network_received=52.7,
        timestamp=datetime.now()
    )

    # Add all metrics
    db.session.add_all([
        metric1,
        metric2,
        metric3,
        metric4,
        metric5
    ])

    # Save changes
    db.session.commit()

    print("5 temporary metric records inserted successfully!")