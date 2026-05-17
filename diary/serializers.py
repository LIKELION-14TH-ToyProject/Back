from rest_framework import serializers
from .models import Post, Comment, Tag



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id', 'post', 'username', 'comment_text', 'created_at'
        )



class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    tag_names = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False
        )
    
    tag_list = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'date', 'body', 'language', 'photo', 'comments', 'tag_names', 'tag_list'
        )


    def get_tag_list(self, obj):
        return [tag.name for tag in obj.tags.all()]
    
    def create(self, validated_data):
        tag_names = validated_data.pop('tag_names', [])

        post = Post.objects.create(**validated_data)

        for tag_name in tag_names:
            tag_name = tag_name.strip()

            if tag_name:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)

        return post
    
    def update(self, instance, validated_data):
        tag_names = validated_data.pop('tag_names', None)

        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.language = validated_data.get('language', instance.language)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()

        if tag_names is not None: # 태그 값이 실제로 들어왔을 떄만 수정
            instance.tags.clear()

            for tag_name in tag_names:
                tag_name = tag_name.strip()

                if tag_name:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    instance.tags.add(tag)
        
            # 게시글이 하나도 없는 태그 삭제
            Tag.objects.filter(posts__isnull=True).delete()


        return instance
