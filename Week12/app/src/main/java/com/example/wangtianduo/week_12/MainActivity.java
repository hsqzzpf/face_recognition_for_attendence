package com.example.wangtianduo.week_12;
//TODO 10 PUT IN YOUR OWN PACKAGE STATEMENT

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.style.UpdateLayout;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;
import com.google.firebase.storage.UploadTask;

import java.io.ByteArrayOutputStream;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.Set;

public class MainActivity extends AppCompatActivity {

    Button buttonPart1;
    Button buttonPart2AddPicture;
    Button buttonPart2GetPicture;
    ImageView imageViewPart2;
    String TAG = "my firebase app";

    //TODO 10.1 Get a reference to the root node of the firebase database
    DatabaseReference mRootDatabaseRef = FirebaseDatabase.getInstance().getReference();

    //TODO 10.6 Get a reference to the root note of the firebase storage
    StorageReference storageReference;

    DatabaseReference databaseReferencePart1;
    DatabaseReference databaseReferencePart2;
    DatabaseReference databaseReferenceSampleNodeValue;
    ArrayList<String> randomStrings;

    String CHILD_NODE_PART1 = "Part1";
    String CHILD_NODE_PART2 = "Part2";

    String SAMPLE_NODE  = "Pokemon";
    TextView textViewSampleNodeValue;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //TODO 10.0 Example
        textViewSampleNodeValue = findViewById(R.id.textViewSampleNodeValue);
        databaseReferenceSampleNodeValue = mRootDatabaseRef.child(SAMPLE_NODE);
        databaseReferenceSampleNodeValue.setValue("Psyduck");

        databaseReferenceSampleNodeValue.addListenerForSingleValueEvent(
                new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                        String text = dataSnapshot.getKey() + ":" + dataSnapshot.getValue();
                        textViewSampleNodeValue.setText((String) dataSnapshot.getValue());
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError databaseError) {

                    }
                }
        );


        //TODO 10.2 initialize the array of strings

        randomStrings = new ArrayList<>();
        randomStrings.add("Mozart");
        randomStrings.add("Ada LoveLace");
        randomStrings.add("Beethoven");

        //TODO 10.3 get a reference to the child node
        mRootDatabaseRef.child(CHILD_NODE_PART1);

        //TODO 10.4 Get a reference to the “Add a Random Word” button, set up the OnClickListener and upload a random word to firebase.


        //TODO 10.8 Build a HashMap object with your data

        //TODO 10.9 Get reference to the root of the child node part 2

        //TODO 10.10 Get reference to the Add Pictures button and write code to upload the HashMap data when button is clicked
        //TODO 10.11  Loop through each entry in the hashmap and do the necessary to upload the image to firebase


        //TODO 10.12 Get a reference to the widgets and write code to download an image randomly when the Get Picture button is clicked




    }

    @Override
    protected void onStart() {
        super.onStart();
        Log.i(TAG,"onStart");

        //TODO 10.5 invoke addValueEventListener on databaseReferencePart1
        //TODO 10.5 get a reference to the LinearLayoutpart1 and dynanmicaly




    }

    //TODO 10.7 Write a static inner class for Part2

    static class ImageData{

        String filename;
        String description;

        ImageData(String filename, String description){
            this.filename = filename;
            this.description = description;

        }
    }

    void uploadFileToFirebaseStorage(String name, String path){

        int resID = getResources().getIdentifier(name , "drawable", getPackageName());

        Bitmap bitmap = BitmapFactory.decodeResource(
                MainActivity.this.getResources(),
                resID);

        Log.i(TAG, "Res ID " + resID);
        Log.i(TAG, "Bitmap " + bitmap.toString());

        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        bitmap.compress(Bitmap.CompressFormat.JPEG, 100, byteArrayOutputStream);
        byte[] data = byteArrayOutputStream.toByteArray();

        StorageReference imageRef = storageReference.child(path);

        UploadTask uploadTask = imageRef.putBytes(data);

        uploadTask.addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Toast.makeText(MainActivity.this,
                        "cannot upload",
                        Toast.LENGTH_LONG).show();
            }
        }).addOnSuccessListener(new OnSuccessListener<UploadTask.TaskSnapshot>() {
            @Override
            public void onSuccess(UploadTask.TaskSnapshot taskSnapshot) {
                Toast.makeText(MainActivity.this,
                        "upload success",
                        Toast.LENGTH_LONG).show();

            }
        });

    }

    void downloadFromFirebaseStorage(String path, final ImageView imageView){

        final StorageReference imageRef = storageReference.child(path);

        final long ONE_MB = 1024*1024;
        imageRef.getBytes(ONE_MB).addOnSuccessListener(new OnSuccessListener<byte[]>() {
            @Override
            public void onSuccess(byte[] bytes) {

                Bitmap bitmap = BitmapFactory.decodeByteArray(bytes, 0, bytes.length);
                imageView.setImageBitmap(bitmap);


            }
        }).addOnFailureListener(new OnFailureListener() {
            @Override
            public void onFailure(@NonNull Exception e) {
                Toast.makeText(MainActivity.this,
                        "cannot download",
                        Toast.LENGTH_LONG).show();
            }
        });
    }



}
