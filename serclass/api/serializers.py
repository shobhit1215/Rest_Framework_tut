from rest_framework import serializers
from .models import Singer,Song
class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        fields = ['id','title','duration',]
class SingerSerializer(serializers.ModelSerializer):
    #with the below command we are connecting id of songs to their title
    # song = serializers.StringRelatedField(many=True,read_only=True)

    #with the below command song field will have id
    # song = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    #With the beloy command song field will have hyperlink of that song
    # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    
    #With the below command song field will have value defined in slug field
    # song = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')

    #We can get detail of all the songs by nested serializers
    song = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']
        #in the above fields we are accessing the related name of models 


    
