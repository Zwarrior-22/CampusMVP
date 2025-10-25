from app import app, db
from models import User, Post
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

def seed_database():
    with app.app_context():
        print("Seeding database with sample data...")
        
        if User.query.filter_by(username='dramaclub').first():
            print("Sample data already exists. Skipping seeding.")
            return
        
        club1 = User(
            username='dramaclub',
            password_hash=generate_password_hash('password123'),
            full_name='Sarah Johnson',
            organization='Drama Club',
            role='club'
        )
        
        club2 = User(
            username='techclub',
            password_hash=generate_password_hash('password123'),
            full_name='Raj Patel',
            organization='Tech & Innovation Club',
            role='club'
        )
        
        club3 = User(
            username='sportsclub',
            password_hash=generate_password_hash('password123'),
            full_name='Mike Chen',
            organization='Sports Committee',
            role='club'
        )
        
        admin_user = User.query.filter_by(username='admin').first()
        
        db.session.add_all([club1, club2, club3])
        db.session.commit()
        
        posts = [
            Post(
                title='Annual Cultural Fest 2025',
                body='Get ready for the biggest cultural event of the year! Join us for three days of music, dance, drama, and fun. Registrations are now open for all performance categories.',
                post_type='event',
                author_id=club1.id,
                is_official=False,
                event_date=(datetime.now() + timedelta(days=15)).date(),
                event_time='10:00 AM',
                event_location='Main Auditorium'
            ),
            Post(
                title='Important: Fee Payment Deadline',
                body='This is a reminder that the last date for semester fee payment is approaching. Please ensure all fees are paid by the deadline to avoid late penalties. Visit the accounts section for any queries.',
                post_type='notice',
                author_id=admin_user.id,
                is_official=True
            ),
            Post(
                title='Hackathon 2025: Code for Change',
                body='Are you ready to solve real-world problems? Join our 24-hour hackathon and compete for exciting prizes! Open to all students. Teams of 2-4 members. Limited slots available.',
                post_type='event',
                author_id=club2.id,
                is_official=False,
                event_date=(datetime.now() + timedelta(days=8)).date(),
                event_time='9:00 AM',
                event_location='Computer Science Block, Lab 3'
            ),
            Post(
                title='Library Timing Update',
                body='The central library will now remain open until 10 PM on weekdays to accommodate exam preparation. Weekend timings remain unchanged (9 AM - 6 PM).',
                post_type='notice',
                author_id=admin_user.id,
                is_official=True
            ),
            Post(
                title='Inter-College Basketball Tournament',
                body='Calling all basketball enthusiasts! Tryouts for the college team are scheduled for this weekend. Show your skills and represent our college at the state-level tournament.',
                post_type='event',
                author_id=club3.id,
                is_official=False,
                event_date=(datetime.now() + timedelta(days=3)).date(),
                event_time='6:00 AM',
                event_location='Basketball Court'
            ),
            Post(
                title='Guest Lecture: AI in Healthcare',
                body='The Computer Science Department invites you to an insightful session on Artificial Intelligence in Healthcare by Dr. Emily Roberts from Stanford University. All students welcome!',
                post_type='event',
                author_id=club2.id,
                is_official=False,
                event_date=(datetime.now() + timedelta(days=5)).date(),
                event_time='2:00 PM',
                event_location='Seminar Hall B'
            ),
            Post(
                title='Campus Cleanliness Drive',
                body='Join us in making our campus greener and cleaner! Volunteers needed for our monthly cleanliness drive. Community service hours will be awarded to all participants.',
                post_type='event',
                author_id=admin_user.id,
                is_official=True,
                event_date=(datetime.now() + timedelta(days=2)).date(),
                event_time='7:00 AM',
                event_location='Main Gate Assembly Point'
            )
        ]
        
        db.session.add_all(posts)
        db.session.commit()
        
        print("Database seeded successfully!")
        print(f"Added {len(posts)} posts")
        print("\nSample Accounts:")
        print("- Admin: username=admin, password=admin123")
        print("- Drama Club: username=dramaclub, password=password123")
        print("- Tech Club: username=techclub, password=password123")
        print("- Sports: username=sportsclub, password=password123")

if __name__ == '__main__':
    seed_database()
