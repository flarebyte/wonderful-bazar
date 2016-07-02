package com.flarebyte.azalea.engine.scene;

public class SceneBuffer {
    public Scene current;
    public Scene previous;
    public Scene next;

    public void pushScene(Scene scene) {
	previous = current;
	current = next;
	next = scene;
    }
}
