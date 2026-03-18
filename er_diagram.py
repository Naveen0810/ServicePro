#!/usr/bin/env python3
"""
ServicePro ER Diagram Generator
Creates an Entity-Relationship diagram for the ServicePro database schema
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

def create_er_diagram():
    """Create and save ER diagram for ServicePro database"""
    
    # Set up the figure
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 15)
    ax.axis('off')
    
    # Define colors
    primary_color = '#2563eb'
    entity_color = '#f0f9ff'
    relationship_color = '#fef3c7'
    attribute_color = '#f0fdf4'
    
    # Entity positions
    entities = {
        'User': (2, 12),
        'ServiceProvider': (8, 12),
        'Service': (14, 12),
        'Booking': (5, 7),
        'Review': (11, 7),
        'Message': (2, 3),
        'VerificationDocument': (8, 3),
        'Notification': (14, 3)
    }
    
    # Draw entities
    for entity_name, (x, y) in entities.items():
        # Entity box
        entity_box = FancyBboxPatch(
            (x-1.2, y-0.8), 2.4, 1.6,
            boxstyle="round,pad=0.1",
            facecolor=entity_color,
            edgecolor=primary_color,
            linewidth=2
        )
        ax.add_patch(entity_box)
        ax.text(x, y, entity_name, ha='center', va='center', 
                fontsize=10, fontweight='bold', color=primary_color)
    
    # Draw relationships and connections
    connections = [
        # User to ServiceProvider (1:1)
        {'from': 'User', 'to': 'ServiceProvider', 'type': '1:1', 'label': 'has'},
        
        # User to Booking (1:N)
        {'from': 'User', 'to': 'Booking', 'type': '1:N', 'label': 'makes'},
        
        # ServiceProvider to Booking (1:N)
        {'from': 'ServiceProvider', 'to': 'Booking', 'type': '1:N', 'label': 'receives'},
        
        # Service to Booking (1:N)
        {'from': 'Service', 'to': 'Booking', 'type': '1:N', 'label': 'booked_for'},
        
        # Booking to Review (1:1)
        {'from': 'Booking', 'to': 'Review', 'type': '1:1', 'label': 'has'},
        
        # User to Review (1:N)
        {'from': 'User', 'to': 'Review', 'type': '1:N', 'label': 'writes'},
        
        # ServiceProvider to Review (1:N)
        {'from': 'ServiceProvider', 'to': 'Review', 'type': '1:N', 'label': 'receives'},
        
        # User to Message (1:N - sender)
        {'from': 'User', 'to': 'Message', 'type': '1:N', 'label': 'sends'},
        
        # User to Message (1:N - receiver)
        {'from': 'User', 'to': 'Message', 'type': '1:N', 'label': 'receives', 'curve': True},
        
        # ServiceProvider to VerificationDocument (1:N)
        {'from': 'ServiceProvider', 'to': 'VerificationDocument', 'type': '1:N', 'label': 'uploads'},
        
        # User to Notification (1:N)
        {'from': 'User', 'to': 'Notification', 'type': '1:N', 'label': 'gets'},
    ]
    
    # Draw connections
    for conn in connections:
        from_pos = entities[conn['from']]
        to_pos = entities[conn['to']]
        
        if conn.get('curve'):
            # Curved line for self-referencing relationships
            ax.annotate('', xy=to_pos, xytext=from_pos,
                       arrowprops=dict(arrowstyle='->', lw=1.5, color='gray',
                                     connectionstyle="arc3,rad=.3"))
        else:
            # Straight line
            ax.annotate('', xy=to_pos, xytext=from_pos,
                       arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'))
        
        # Add relationship label
        mid_x = (from_pos[0] + to_pos[0]) / 2
        mid_y = (from_pos[1] + to_pos[1]) / 2
        ax.text(mid_x, mid_y + 0.3, conn['label'], 
                ha='center', va='center', fontsize=8, style='italic')
        ax.text(mid_x, mid_y - 0.3, conn['type'], 
                ha='center', va='center', fontsize=8, fontweight='bold')
    
    # Add entity details (attributes)
    entity_details = {
        'User': [
            'PK: id (INT)',
            'name (VARCHAR)',
            'email (VARCHAR)',
            'password (VARCHAR)',
            'role (ENUM)',
            'address (TEXT)',
            'pincode (VARCHAR)',
            'phone (VARCHAR)',
            'created_at (DATETIME)'
        ],
        'ServiceProvider': [
            'PK: id (INT)',
            'FK: user_id (INT)',
            'service_categories (JSON)',
            'service_pincodes (JSON)',
            'status (ENUM)',
            'verification_status (ENUM)',
            'availability (JSON)',
            'hourly_rate (FLOAT)',
            'description (TEXT)',
            'experience_years (INT)'
        ],
        'Service': [
            'PK: id (INT)',
            'category (VARCHAR)',
            'description (TEXT)',
            'base_price (FLOAT)',
            'is_active (BOOLEAN)'
        ],
        'Booking': [
            'PK: id (INT)',
            'FK: user_id (INT)',
            'FK: provider_id (INT)',
            'FK: service_id (INT)',
            'booking_date (DATETIME)',
            'status (ENUM)',
            'address (TEXT)',
            'total_amount (FLOAT)',
            'created_at (DATETIME)'
        ],
        'Review': [
            'PK: id (INT)',
            'FK: booking_id (INT)',
            'FK: user_id (INT)',
            'FK: provider_id (INT)',
            'rating (INT)',
            'comments (TEXT)',
            'created_at (DATETIME)'
        ],
        'Message': [
            'PK: id (INT)',
            'FK: sender_id (INT)',
            'FK: receiver_id (INT)',
            'message (TEXT)',
            'timestamp (DATETIME)',
            'is_read (BOOLEAN)'
        ],
        'VerificationDocument': [
            'PK: id (INT)',
            'FK: provider_id (INT)',
            'document_type (VARCHAR)',
            'file_path (VARCHAR)',
            'uploaded_at (DATETIME)',
            'admin_notes (TEXT)',
            'status (ENUM)'
        ],
        'Notification': [
            'PK: id (INT)',
            'FK: user_id (INT)',
            'title (VARCHAR)',
            'message (TEXT)',
            'type (ENUM)',
            'is_read (BOOLEAN)',
            'created_at (DATETIME)'
        ]
    }
    
    # Add attribute boxes
    for entity_name, (x, y) in entities.items():
        attributes = entity_details[entity_name]
        
        # Create attribute box
        attr_height = len(attributes) * 0.25 + 0.5
        attr_box = FancyBboxPatch(
            (x-1.5, y-2.5-attr_height), 3, attr_height,
            boxstyle="round,pad=0.05",
            facecolor=attribute_color,
            edgecolor='#059669',
            linewidth=1
        )
        ax.add_patch(attr_box)
        
        # Add attributes
        for i, attr in enumerate(attributes):
            attr_y = y-2-attr_height/2 + i*0.25 + 0.15
            if attr.startswith('PK:'):
                color = '#dc2626'
                fontweight = 'bold'
            elif attr.startswith('FK:'):
                color = '#2563eb'
                fontweight = 'bold'
            else:
                color = '#374151'
                fontweight = 'normal'
            
            ax.text(x, attr_y, attr, ha='center', va='center', 
                    fontsize=7, color=color, fontweight=fontweight)
    
    # Add title and legend
    ax.text(10, 14.5, 'ServicePro Database - Entity Relationship Diagram', 
            ha='center', va='center', fontsize=16, fontweight='bold', color=primary_color)
    
    # Legend
    legend_items = [
        ('PK', 'Primary Key', '#dc2626'),
        ('FK', 'Foreign Key', '#2563eb'),
        ('1:1', 'One-to-One', '#374151'),
        ('1:N', 'One-to-Many', '#374151')
    ]
    
    for i, (label, desc, color) in enumerate(legend_items):
        ax.text(1, 0.5 - i*0.3, f'{label}: {desc}', 
                fontsize=9, color=color, fontweight='bold')
    
    # Add constraints and business rules
    constraints_text = """
Business Rules & Constraints:
• User.role ∈ {'user', 'provider', 'admin'}
• ServiceProvider.status ∈ {'pending', 'approved', 'rejected'}
• Booking.status ∈ {'pending', 'accepted', 'in_progress', 'completed', 'cancelled'}
• Review.rating ∈ {1, 2, 3, 4, 5}
• Message.is_read ∈ {true, false}
• VerificationDocument.document_type ∈ {'government_id', 'business_license', 'profile_photo'}
• Notification.type ∈ {'system', 'approved', 'rejected', 'message'}
• User.email is unique across all users
• Each User can have at most one ServiceProvider profile
• Each Booking can have at most one Review
    """
    
    ax.text(10, 0.5, constraints_text, ha='center', va='center', 
            fontsize=8, color='#6b7280', style='italic',
            bbox=dict(boxstyle="round,pad=0.5", facecolor='#f9fafb', edgecolor='#d1d5db'))
    
    plt.tight_layout()
    plt.savefig('d:/ServicePro/servicepro_er_diagram.png', dpi=300, bbox_inches='tight')
    plt.savefig('d:/ServicePro/servicepro_er_diagram.pdf', bbox_inches='tight')
    plt.show()
    
    print("ER Diagram generated successfully!")
    print("Files saved:")
    print("- servicepro_er_diagram.png (high resolution)")
    print("- servicepro_er_diagram.pdf (vector format)")

if __name__ == "__main__":
    create_er_diagram()
